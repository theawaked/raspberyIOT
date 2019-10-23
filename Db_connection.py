import sqlite3
from datetime import datetime as datetime

#this file contains methods for inserting sensor data into an sqlite database, import this to another file to use the functions.
#running this file wil create the database and table for storing the sensordata

conn=sqlite3.connect('sensordata')
c = conn.cursor()

table_create_string = """CREATE TABLE IF NOT EXISTS sensorreadings(
                            id integer PRIMARY KEY,
                            temperature NUMERIC,
                            humidity NUMERIC,
                            pressure NUMERIC,
                            datetime datetime
                        );"""
    
#tables_insert_string = """INSERT INTO sensorreadings(temperature, humidity, pressure)VALUES(1,1,1)"""

try:
    c.execute(table_create_string)
except sqlite3.Error as e:
        print(e)

# try:
#     c.execute(tables_insert_string)
# except sqlite3.IntegrityError as e:
#         print(e)
# conn.commit()

def create_connection():
    try:
        conn=sqlite3.connect('sensordata')
    except sqlite3.Error as e:
     print(e)

    #c = conn.cursor()
    return conn

def insert_dbvalues(connection,temperature,humidity,pressure):
       # tables_insert_string = """INSERT INTO sensorreadings(temperature, humidity, pressure, datetime)VALUES({},{},{},{});""".format(temperature,humidity,pressure,datetime.now())
       datetime1 = datetime.now()
       data_tuple = (temperature, humidity, pressure)
       tables_insert_string = """INSERT INTO sensorreadings(temperature, humidity, pressure)VALUES(?,?,?)"""

   
       #print(tables_insert_string)
       c = connection.cursor()
       try:
           c.execute(tables_insert_string, data_tuple)
       except sqlite3.IntegrityError as e:
           print(e)
       
       c.commit()

       c.close()
       


# insert_dbvalues(create_connection(),1,2,3)
# try:
#     c.execute("INSERT INTO {tn} ({cn1}, {cn2}, {cn3}) VALUES (123456, 123456, 123456)".\
#         format(tn=table_name, cn1=temperature_column, cn2=humidity_column, cn3=pressure_column))
# except sqlite3.IntegrityError:
#     print('ERROR: integerityError')


conn.close()