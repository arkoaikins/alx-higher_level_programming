#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Create a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object to allow the script to execute SQL statements
    c = db.cursor()
    # retrieve all states table and order them
    c.execute("SELECT * FROM states")
    # retrieve all rows of the states table
    rows = c.fetchall()
    # iterate through the rows and print them one by one
    for row in rows:
        print(row)
    # close to clean up resources
    c.close()
    db.close()
