'''
class for connections and basic operations
'''
import mysql.connector
class Operation:
    '''
        createdb() -> creates practice database
        createtable(query) -> use if exists query to create the table
        insertone(query)-> insert one row
        insertmany(query,list_of_tuple_of_values) -> insert many rows
        selectone(query) -> select a particular row from the table
        selectall(query)-> returns all the rows 
        update(query)-> updates rows
        delete(query)-> delete rows

    '''
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = 'localhost',user = 'root',password = '1234')
            print('connection established!')
            self.cursor = self.conn.cursor()
            self.createdb()
            self.cursor.execute('use practice')
        except:
            print('Error occured in connection/db creation')            

    def createdb(self):
        self.cursor.execute('create database if not exists practice')
        print('Database created!')
        self.cursor.execute('show databases')
        for i in self.cursor:
            print(i)

    def createtable(self,query):
        self.cursor.execute(query)
        print('table created!!')

    
    def insertone(self,*values):
        # query = values[0]
        query = values[0]
        self.cursor.execute(query)
        self.conn.commit()
        print('number of rows inserted:',self.cursor.rowcount)

    def insertmany(self,*values):
        query = values[0]
        val = values[1]
        self.cursor.executemany(query,val)
        self.conn.commit()
        print('No of rows inserted:',self.cursor.rowcount)

    def selectone(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(result)
    
    def selectall(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
    
    def update(self,query):
        self.cursor.execute(query)
        self.conn.commit()
        print('Rows Updated:',self.cursor.rowcount)

    def deleterows(self,query):
        self.cursor.execute(query)
        self.conn.commit()
        print('Rows Deleted:',self.cursor.rowcount)

    def droptable(self,query):
        self.cursor.execute(query)
        self.conn.commit()
        print('Table Deleted successfully!')

    def dropdatabase(self):
        self.cursor.execute('''
        drop database practice
        ''')
        self.conn.commit()
        print('Database deleted!!')


