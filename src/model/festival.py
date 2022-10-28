# Standard library imports
import asyncio
import logging

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

    async def connect(self):
        try:
            while True:
                conn =self.__postgreSQL_pool.getconn()
                if conn:
                    logger.warning('Connection opened successfully.')
                    break
                await asyncio.sleep(0.5)

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            return conn

    def disConnect(self, conn):
        logger.info('put conn')
        self.__postgreSQL_pool.putconn(conn)

    #Read data from festival table
    async def getFestivals(self):
        try:
            sql = """ SELECT * FROM festivals"""
            #conn = await self.connect()
            conn = await self.connect()
            with conn.cursor() as cur:
                cur.execute(sql)
                records = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)
            return records

    async def getFestivalByID(self, id):
        try:
            sql = """ SELECT * FROM festivals WHERE id=%s """
            conn = await self.connect()

            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                record = cur.fetchone()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)
            return record

    async def getFestivalFree(self):
        try:
            sql = """ SELECT id, name, startdate, enddate FROM festivals WHERE free=true """
            conn = await self.connect()

            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                record = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)
            return record


 

    #inert data into rename table
    async def insertFestival(self, name, start, end, area, location, free, bands, notes):
        logger.debug("############ insert festival #############")
        try:
            sql = """ INSERT INTO festivals (name, startdate, enddate, area, location, free, bands, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
            conn = await self.connect()

            insertTuple = (name, start, end, area, location, free, bands, notes)

            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()

            logger.info('insert successfully.')

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.warning('insert festivals failed. roll back')
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)

    async def updateFestival(self, id, name, start, end, area, location, free, bands, notes):
        logger.debug("############ update festival #############")
        try:
            sql = """ UPDATE festivals SET name=%s, startdate=%s, enddate=%s, area=%s, location=%s, free=%s, bands=%s, notes=%s WHERE id=%s"""
            conn = await self.connect()

            updateTuple = (name, start, end, area, location, free, bands, notes, id)

            with conn.cursor() as cur:
                cur.execute(sql, updateTuple)
                conn.commit()

            logger.info('update successfully.')

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.warning('update festivals failed. roll back')
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn)

    #delete data from rename table
    async def deleteFestival(self, id):
        try:
            sql = """ DELETE FROM festivals WHERE id=%s """

            conn = await self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                #rows_deleted = cur.rowcount
                #print(rows_deleted)

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.disConnect(conn) 
        
        

if __name__ == '__main__':
    pass