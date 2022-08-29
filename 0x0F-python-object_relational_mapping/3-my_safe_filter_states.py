#!/usr/bin/python3
"""
takes in arguments and displays all values in the states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    s = cursor.fetchall()
    for a in s:
        print(a)
    cursor.close()
    db.close()
