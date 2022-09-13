import logging
import psycopg2
import logging

logger = logging.getLogger()

class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host     = '127.0.0.1'
        self.username = 'postgres'
        self.password = '5598'
        self.port     = '5432'
        self.dbname   = 'postgres'
        self.conn     = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )

                cursor = self.conn.cursor()
                # Print PostgreSQL details
                print("PostgreSQL server information")
                print(self.conn.get_dsn_parameters(), "\n")
                # Executing a SQL query
                cursor.execute("SELECT version();")
                # Fetch result
                record = cursor.fetchone()
                print("You are connected to - ", record, "\n")

            except psycopg2.DatabaseError as e:
                logger.error(e)
                raise e
            finally:
                logger.info('Connection opened successfully.')
    
    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records

if __name__ == '__main__':
    db = Database()
    db.connect()