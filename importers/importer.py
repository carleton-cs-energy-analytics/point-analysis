import os
import psycopg2
from decoders.siemens_master import get_points

CONN = psycopg2.connect(host=os.environ.get('DATABASE_HOST') or '',
                        dbname=os.environ.get('DATABASE_NAME') or 'energy-dev',
                        user=os.environ.get('DATABASE_USER') or '',
                        password=os.environ.get('DATABASE_PASSWORD') or '')


def try_cast_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


def execute_and_commit(query, vars):
    """Runs the given query on the database, then commits the database connection.

    :param query: The SQL query
    :param vars: Any values that need to be injected into the SQL query
    """
    with CONN.cursor() as curs:
        curs.execute(query, vars)
        CONN.commit()


def get_id_of_unit(unit, measurement):
    """Queries the database for the ID of the value_unit with the given unit and measurement"""
    with CONN.cursor() as curs:
        query = "SELECT value_unit_id FROM value_units WHERE unit = %s AND measurement = %s"
        vars = (unit, measurement)
        curs.execute(query, vars)
        results = curs.fetchall()
        if len(results) == 0:
            return None
        else:
            return results[0][0]


def get_id_of(table, name, building_id=None, room_id=None):
    """Queries the database for the ID of the row in the given table with the given name
    If a building_id or room_id are given, it is added as requirements to the WHERE clause.
    """
    with CONN.cursor() as curs:
        query = "SELECT " + table[:-1] + "_id FROM " + table + " WHERE name = %s"
        vars = (name,)
        if building_id is not None:
            query += " and building_id = %s"
            vars += (building_id,)
        elif room_id is not None:
            query += " and room_id = %s"
            vars += (room_id,)
        curs.execute(query, vars)
        results = curs.fetchall()
        if len(results) == 0:
            return None
        else:
            return results[0][0]


def import_point(points):
    for point in points:
        point.building_name = point.building_name or "UnID'd Building"  # UnID'd := Unidentified
        building_id = get_id_of("buildings", point.building_name)
        if building_id is None:
            execute_and_commit("""INSERT INTO buildings (name) VALUES (%s)""",
                               (point.building_name,))
            building_id = get_id_of("buildings", point.building_name)

        # use somewhere: {'floor': point.room_floor, 'building_id': building_id}
        point.room_name = point.room_name or "UnID'd Room in " + point.building_name
        room_id = get_id_of("rooms", point.room_name, building_id=building_id)
        if room_id is None:
            execute_and_commit(
                """INSERT INTO rooms (name, building_id, floor) VALUES (%s, %s, %s)""",
                (point.room_name, building_id, try_cast_int(point.room_floor)))
            room_id = get_id_of("rooms", point.room_name, building_id=building_id)

        # {'room_id': room_id}
        point.device_name = point.device_name or "UnID'd Device in " + point.building_name \
                            + " " + point.room_name
        device_id = get_id_of("devices", point.device_name, room_id=room_id)
        if device_id is None:
            execute_and_commit("""INSERT INTO devices (name, room_id) VALUES (%s, %s)""",
                               (point.device_name, room_id))
            device_id = get_id_of("devices", point.device_name, room_id=room_id)

        reordering_map = {
            "OCC_UNOCC": "UNOCC_OCC",
            "ON_OFF": "OFF_ON",
            "OPEN_CLOSED": "CLOSED_OPEN",
            "DAY_NIGHT": "NIGHT_DAY",
            "ENABLE_DISABL": "DISABL_ENABLE",
            "DISABL_ENABL": "DISABL_ENABLE"
        }

        if point.value_type in reordering_map.keys():
            point.value_type = reordering_map[point.value_type]
        value_type_id = get_id_of("value_types", point.value_type)
        if value_type_id is None:
            raise Exception("value_type of name %s not found" % point.value_type)

        value_units_id = get_id_of_unit(point.get_unit(), point.get_measurement())
        if value_units_id is None and point.get_unit() is not None and point.get_measurement() is not None:
            raise Exception("value_units of unit %s and measurement %s not found"
                            % (point.get_unit(), point.get_measurement()))

        execute_and_commit(
            """
            INSERT INTO points (name, device_id, value_type_id, value_unit_id) 
            VALUES(%s, %s, %s, %s)
            """, (point.point_name, device_id, value_type_id, value_units_id))

        point_id = get_id_of("points", point.point_name)

        for (table, id, tags) in [('buildings', building_id, point.get_building_tags()),
                                  ('rooms', room_id, point.get_room_tags()),
                                  ('devices', device_id, point.get_device_tags()),
                                  ('points', point_id, point.get_point_tags())]:
            for tag in tags:
                if tag is not None:
                    tag_id = get_id_of("tags", tag)
                    if tag_id is None:
                        execute_and_commit("""INSERT INTO tags (name) VALUES (%s)""", (tag,))
                        tag_id = get_id_of("tags", tag)

                    execute_and_commit(
                        "INSERT INTO " + table + "_tags (" + table[:-1] + "_id, tag_id) " +
                        "VALUES (%s, %s) ON CONFLICT DO NOTHING", (id, tag_id))


def main():
    import_point(get_points())


if __name__ == '__main__':
    main()
