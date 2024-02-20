#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa.

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Holberton school as a test for the implementation
of MySQLdb module with hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \                       
                ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
