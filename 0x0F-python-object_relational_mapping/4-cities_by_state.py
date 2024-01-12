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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id;")

    results = cur.fetchall()
    for row in results:
        print(row)
