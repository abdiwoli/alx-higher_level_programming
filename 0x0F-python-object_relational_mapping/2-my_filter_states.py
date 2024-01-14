#!/usr/bin/python3
""" search stste """
import MySQLdb
import sys


if __name__ == "__main__" and len(sys.argv) == 5:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    query = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin = {} ORDER BY id;".format("%s")

    cur.execute(query, (search,))
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()
