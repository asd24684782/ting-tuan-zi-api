# Standard library imports
import logging
import json
import uuid

# Third party imports
import psycopg2
from psycopg2 import pool

# Local application imports


logger = logging.getLogger()

class Festival:
    """PostgreSQL Database class."""

    def __init__(self, host, user, password, port, dbName):
        self.__host     = host
        self.__user     = user
        self.__password = password
        self.__port     = port
        self.__dbName   = dbName
        try:
            self.__postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, 
                                                                user=self.__user,
                                                                password=self.__password,
                                                                host=self.__host,
                                                                port=self.__port,
                                                                database=self.__dbName)
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
    
    def disConnect(self, conn):
        self.__postgreSQL_pool.putconn(conn)

    #Read data from festival table
    def getFestivals(self):
        try:
            sql = """ SELECT * FROM festivals"""
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
    def insertFestival(self, name, date, location, bands):
        try:
            sql = """ INSERT INTO festivals (name, date, location, bands) VALUES (%s, %s, %s, %s) """

            insertTuple = (name, date, location, bands)

            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.warning('insert festivals failed. roll back')
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