"""Work with oracle atoll db."""

import os
from collections import namedtuple

import cx_Oracle


class Atoll(object):
    """Work with oralce atoll db."""

    def __init__(self, delete_sql, insert_sql, select_sql=''):
        """
        Construct new atoll object.

        Args:
            delete_sql: string
            insert_sql: string
            select_sql: string
        """
        self.delete_sql = delete_sql
        self.insert_sql = insert_sql
        self.select_sql = select_sql

    def execute_sql(self, sql_command, sql_type, cells=()):
        """
        Execute sql command for atoll db.

        Args:
            sql_command: string
            sql_type: string
            cells: deque object

        Returns:
            tuple
        """
        atoll_dsn = cx_Oracle.makedsn(
            os.getenv('ATOLL_HOST'),
            os.getenv('ATOLL_PORT'),
            service_name=os.getenv('SERVICE_NAME'),
        )
        with cx_Oracle.connect(
            user=os.getenv('ATOLL_LOGIN'),
            password=os.getenv('ATOLL_PASSWORD'),
            dsn=atoll_dsn,
        ) as connection:
            cursor = connection.cursor()
            if sql_type == 'select':
                cursor.execute(sql_command)
                cursor.rowfactory = namedtuple(
                    'PhysicalParameters',
                    ['cell_name', 'azimut', 'height', 'longitude', 'latitude'],
                )
                return cursor.fetchall()
            elif sql_type == 'delete':
                cursor.execute(sql_command)
            else:
                cursor.executemany(sql_command, cells)
            connection.commit()

    def delete_data(self):
        """Delete data."""
        self.execute_sql(self.delete_sql, 'delete')

    def update_network_live(self, cells):
        """
        Insert new cells to atoll db.

        Args:
            cells: deque object
        """
        self.execute_sql(self.insert_sql, 'insert', cells)

    def handle_atoll_data(self, select_data):
        """
        Handle selected atoll data to dict.

        Args:
            select_data: list of tuples

        Returns:
            dict
        """
        atoll_data = {}
        for cell in select_data:
            atoll_data[cell.cell_name] = {
                'azimut': cell.azimut,
                'height': cell.height,
                'longitude': cell.longitude,
                'latitude': cell.latitude,
            }
        return atoll_data

    def select_physical_parameters(self):
        """
        Select physical parameters from Atoll.

        Returns:
            dict
        """
        atoll_phys_parameters = self.execute_sql(self.select_sql, 'select')
        return self.handle_atoll_data(atoll_phys_parameters)
