import sqlite3

sqlite_file = '/home/pi/Desktop/program/sensordata'

conn = sqlite3.connect('sensordata')
c = conn.cursor()

table_name = "sensorreadings"
temperature_column = "temperature"
humidity_column = "humidity"
pressure_column = "pressure"

table_create_string = """CREATE TABLE IF NOT EXISTS sensorreadings(
                            id integer PRIMARY KEY,
                            temperature NUMERIC,
                            humidity NUMERIC,
                            pressure NUMERIC,
                            date text,
                            time text 
                        );"""
    
tables_insert_string = """INSERT INTO sensorreadings(termperature, humidity, pressure)VALUES(1,1,1)"""

try:
    c.execute(table_create_string)
except sqlite3.Error as e:
        print(e)

try:
    c.execute(tables_insert_string)
except sqlite3.Error as e:
        print(e)




# try:
#     c.execute("INSERT INTO {tn} ({cn1}, {cn2}, {cn3}) VALUES (123456, 123456, 123456)".\
#         format(tn=table_name, cn1=temperature_column, cn2=humidity_column, cn3=pressure_column))
# except sqlite3.IntegrityError:
#     print('ERROR: integerityError')


conn.close()