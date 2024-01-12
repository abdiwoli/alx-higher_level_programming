#!/usr/bin/python3
""" list all states order by id"""

import sys
import MySQLdb

if __name__ == "__main__" and len(sys.argv) == 4:
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]

    try:
        # Establish a connection to the database
        con = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=passw, db=db)
        cur = con.cursor()

        # Execute the query
        cur.execute("SELECT * FROM cities ORDER BY id;")
        
        # Fetch and print the results
        results = cur.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection in a 'finally' block to ensure they are closed even if an exception occurs
        if cur:
            cur.close()
        if con:
            con.close()
else:
    print("Usage: python script.py <username> <password> <database>")
