#!/usr/bin/python3
""" list all states order by id"""
import MySQLdb
import sys


if __name__ == "__main__" and len(sys.argv) == 4:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    q = """SELECT * FROM states WHERE
           name COLLATE utf8mb4_bin LIKE 'N%' ORDER BY id;"""

    cur.execute(q)
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()
