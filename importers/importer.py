import os
import sys
import psycopg2

CONN = psycopg2.connect(host=os.environ.get('DATABASE_HOST') or '',
                        dbname=os.environ.get('DATABASE_NAME') or 'energy-dev',
                        user=os.environ.get('DATABASE_USER') or '',
                        password=os.environ.get('DATABASE_PASSWORD') or '')


def insert_values(query, items):
    """Used for inserting values into the database. Takes a query and a list of 3-tuples, appends
    the 3-tuples to the query, and then executes and commits it.

    :param query: The SQL query
    :param items: A list of 3-tuples to be appended to the end of the query
    """
    with CONN.cursor() as curs:
        # sanitizes (mogrify) the items, creating strings, and then joins them together with commas
        args_str = ','.join(curs.mogrify("(%s, %s, %s)", item).decode("utf-8") for item in items)
        curs.execute(query + args_str + ";")
        CONN.commit()


def execute_and_commit(query, vars):
    """Runs the given query on the database, then commits the database connection.

    :param query: The SQL query
    :param vars: Any values that need to be injected into the SQL query
    """
    with CONN.cursor() as curs:
        curs.execute(query, vars)
        CONN.commit()


def get_id_of(table, name):
    with CONN.cursor() as curs:
        curs.execute("""SELECT %s_id FROM %s WHERE name = %s""", table, table, name)
        if len(curs.fetchall()) == 0:
            return None
        else:
            return curs.fetchall()[0][0]


def import_point(points):
    for point in points:
        building_id = get_id_of("buildings", point.building_name)
        if building_id is None:
            execute_and_commit("""INSERT INTO buildings (name) VALUES (%s)""", point.building_name)
            building_id = get_id_of("buildings", point.building_name)

        # use somewhere: {'floor': point.room_floor, 'building_id': building_id}
        room_id = get_id_of("rooms", point.room_name)
        if room_id is None:
            execute_and_commit(
                """INSERT INTO rooms (name, building_id, floor) VALUES (%s, %s, %s)""",
                (point.room_name, building_id, point.room_floor))
            room_id = get_id_of("rooms", point.room_name)

        # {'room_id': room_id}
        device_id = get_id_of("devices", point.device_name)
        if device_id is None:
            execute_and_commit("""INSERT INTO devices (name, room_id) VALUES (%s, %s)""",
                               (point.device_name, room_id))
            device_id = get_id_of("devices", point.device_name)

        reordering_map = {
            "OCC_UNOCC": "UNOCC_OCC",
            "ON_OFF": "OFF_ON",
            "OPEN_CLOSED": "CLOSED_OPEN",
            "DAY_NIGHT": "NIGHT_DAY",
            "ENABLE_DISABL": "DISABL_ENABLE"
        }

        if point.value_type in reordering_map.keys():
            point.value_type = reordering_map[point.value_type]
        value_type_id = get_id_of("value_types", point.value_type)
        if value_type_id is None:
            pass

        value_units_id = get_id_of("value_units", point.units)

        execute_and_commit("""
                        INSERT INTO points (name, device_id, value_type_id, value_unit_id) VALUES
                        (%s, %s, %s, %s)
                        """, (point.point_name, device_id, value_type_id, value_units_id))

        point_id = get_id_of("points", point.point_name)

        for (table, id, tags) in [('buildings', building_id, point.building_type),
                                  ('rooms', room_id, point.room_type),
                                  ('devices', device_id, point.device_type),
                                  ('points', point_id, point.point_type)]:
            for tag in tags:
                tag_id = get_id_of("tags", tag)
                if tag_id is None:
                    execute_and_commit("""INSERT INTO tags (name) VALUES (%s)""", tag)
                    tag_id = get_id_of("tags", tag)

                execute_and_commit(
                    """INSERT INTO %s_tags (%s_id, tag_id) VALUES (%s, %s) ON CONFLICT DO NOTHING""",
                    (table, table[:-1], id, tag_id))

