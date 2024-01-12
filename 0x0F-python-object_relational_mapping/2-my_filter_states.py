#!/usr/bin/python3
"""search stste """
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    q = f"SELECT * FROM states WHERE name = '{search}' ORDER BY id;"
    cur.execute(q)
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()
