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
            execute_and_commit("""INSERT INTO %s (name) VALUES (%s)""", "buildings", point.building_name)
            building_id = get_id_of(table, point.building_name)

        # use somewhere: {'floor': point.room_floor, 'building_id': building_id}
        room_id = get_id_of("rooms", point.room_name)
        if room_id is None:
            execute_and_commit("""INSERT INTO %s (name) VALUES (%s)""", "rooms", point.room_name)
            room_id = get_id_of("rooms", point.room_name)

        # {'room_id': room_id}
        device_id = get_id_of("devices", point.device_name)
        if device_id is None:
            execute_and_commit("""INSERT INTO %s (name) VALUES (%s)""", "devices", point.device_name)
            device_id = get_id_of("devices", point.device_name)

        insert("""
                INSERT INTO points (name, device_id, value_type_id, value_unit_id)
                """)


    def add(values):
        """Adds a list of values to the database.

        :param values: A list of 3-tuples in the form `(point_name, timestamp, value)` where values
        are ints, doubles, or enum strings.
        """

        int_values, float_values = Values._prepare_add(values)

        # Only want to insert values if there are values to be inserted for the particular type
        if len(float_values) > 0:
            insert_values("""
                INSERT INTO values (point_id, timestamp, double) VALUES 
                """, float_values)

        if len(int_values) > 0:
            insert_values("""
                INSERT INTO values (point_id, timestamp, int) VALUES 
                """, int_values)
