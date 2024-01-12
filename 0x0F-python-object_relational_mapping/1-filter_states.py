#!/usr/bin/python3
""" list all states order by id"""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    cur.execute("SELECT DISTINCT name, id FROM states WHERE name LIKE 'n%' ORDER BY id;")
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()
