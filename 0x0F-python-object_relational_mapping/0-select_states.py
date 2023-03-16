#!/usr/bin/python3
""" Script that list all states in database
"""
from sys import argv
import MySQLdb

if __name__== '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                        passwd=password, db=database)
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    t = r.fetch_row(maxrows=0)
    for i in t:
        print(i)
