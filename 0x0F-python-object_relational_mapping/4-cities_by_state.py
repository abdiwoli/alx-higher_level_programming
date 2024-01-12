#!/usr/bin/python3
""" list all states order by id"""
import sys
import MySQLdb


if __name__ == "__main__" and len(sys.argv) == 4:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    cur.execute("SELECT id, name FROM cities ORDER BY id;")
    results = cur.fetchall()
    for row in results:
        print(row)
