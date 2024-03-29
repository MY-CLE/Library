import psycopg2
from pathlib import Path
from configparser import ConfigParser

# General Path fix for windows/linux
class DatabaseHandler(object):
    def __init__(self):
        self._config = DatabaseHandler.config()
    
    def config(filename=Path('src/database/database.ini'), section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    def connect(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:
            # read connection parameters
            # connect to the PostgreSQL server
            #print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self._config)
            # create a cursor
            self.cursor = self.conn.cursor()
        # execute a statement
            #print('PostgreSQL database version:')
            self.cursor.execute('SELECT version()')
            
            # display the PostgreSQL database server version
            #db_version = self.cursor.fetchone()
            #print(db_version)
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def parser(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.cursor.close()
            self.conn.close()
    
    def insert(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.cursor.close()
            self.conn.close()

        
if __name__ == '__main__':
    a = DatabaseHandler()
    a.connect()
    print(a.parser("SELECT current_database();"))
