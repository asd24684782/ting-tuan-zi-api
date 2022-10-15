# Standard library imports
import logging
import json
import uuid

# Third party imports
import psycopg2
from psycopg2 import pool

# Local application imports


logger = logging.getLogger()

class rename:
    """PostgreSQL Database class."""

    def __init__(self, host, username, password, port, dbName):
        self.__host     = host
        self.__username = username
        self.__password = password
        self.__port     = port
        self.__dbName   = dbName
        try:
            self.__postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, 
                                                                user=self.__user,
                                                                password=self.__password,
                                                                host=self.__host,
                                                                port=self.__port,
                                                                database=self.__dbname)
            if (self.__postgreSQL_pool):
                print("Connection pool created successfully")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

    def connect(self):
        try:
            conn =self.__postgreSQL_pool.getconn()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            logger.warning('Connection opened successfully.')
            return conn

    
    #Read data from user table
    def getUsers(self):
        try:
            sql = """ SELECT * FROM users"""
            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql)
                records = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)
            logger.warning('connection close')
            return records

    #Read data by id from user table 
    def getUsersByID(self, userID):
        try:
            sql = """ SELECT * FROM users WHERE id=%s"""

            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, (userID,))
                record = cur.fetchone()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)
            logger.warning('connection close')
            return record

    #inert data into rename table
    def insert(self, UUID, JsonStr):
        try:
            sql = """ INSERT INTO users (id, info) VALUES (%s, %s) """
            insertTuple = (UUID, JsonStr)
            
            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                conn.close()
            logger.info('insert successfully.')

    #delete data from rename table
    def delete(self, UUID):
        try:
            sql = """ DELETE FROM rename WHERE id=%s """

            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, (UUID,))
                #rows_deleted = cur.rowcount
                #print(rows_deleted)

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                conn.close()
            logger.info('delete successfully.')     
        
        

if __name__ == '__main__':
    pass