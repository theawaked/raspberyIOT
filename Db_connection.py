import sqlite3

sqlite_file = '/home/pi/Desktop/program/sensordata.'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table_name = "sensorreadings"
temperature_column = "temperature"
humidity_column = "humidity"
pressure_column = "pressure"

try:
    c.execute("INSERT INTO {tn} ({cn1}, {cn2}, {cn3}) VALUES (123456, 123456, 123456)".\
        format(tn=table_name, cn1=temperature_column, cn2=humidity_column, cn3=pressure_column))
except sqlite3.IntegrityError:
    print('ERROR: integerityError')


conn.close()