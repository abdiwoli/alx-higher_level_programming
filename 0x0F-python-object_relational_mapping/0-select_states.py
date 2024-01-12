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
    n = cur.execute("SELECT * FROM states ORDER BY id;")
    for i in range(n):
        print(cur.fetchone())
