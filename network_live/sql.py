"""Work with oracle atoll db."""

import os

import cx_Oracle


class Atoll(object):
    """Work with oralce atoll db."""

    def __init__(self, delete_sql, insert_sql):
        """
        Construct new atoll object.

        Args:
            delete_sql: string
            insert_sql: string
        """
        self.delete_sql = delete_sql
        self.insert_sql = insert_sql

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
                return cursor.execute(sql_command).fetchall()
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
