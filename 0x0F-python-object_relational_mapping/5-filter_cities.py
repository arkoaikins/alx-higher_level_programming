#!/usr/bin/python3
"""
cript that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Create a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object to allow the script to execute SQL statements
    c = db.cursor()
    # retrieving  states table
    c.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    # retrieve all rows of the states table
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    # close to clean up resources
    c.close()
    db.close()
