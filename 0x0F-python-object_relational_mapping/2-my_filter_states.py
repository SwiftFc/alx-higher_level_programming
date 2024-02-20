#!/usr/bin/python3
""" script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
from the database hbtn_0e_0_usa.

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Alx as a test for the implementation
of MySQLdb module with hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
