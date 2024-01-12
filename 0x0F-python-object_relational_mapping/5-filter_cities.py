#!/usr/bin/python3
""" list all states order by id"""
import sys
import MySQLdb


if __name__ == "__main__" and len(sys.argv) == 5:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]
    con = MySQLdb.connect(host='localhost',
                          port=3306, user=user,
                          passwd=passw, db=db)
    cur = con.cursor()
    qr = "SELECT cities.id, cities.name, states.name FROM cities JOIN"
    qr += " states ON cities.state_id = states.id"
    qr += " WHERE states.name = %s ORDER BY cities.id;"
    cur.execute(qr, (state, ))

    results = cur.fetchall()
    for row in results:
        print(row)
