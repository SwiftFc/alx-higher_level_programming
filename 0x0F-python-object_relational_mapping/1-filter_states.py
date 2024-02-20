#!/usr/bin/python3

""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Alx as a test for the implementation
of MySQLdb module with hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
