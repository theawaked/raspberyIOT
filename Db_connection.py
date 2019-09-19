#!/usr/bin/env python

import MySQLdb


db = MySQLdb.connect("localhost", "administrator", "password", "temps")
curs=db.cursor()