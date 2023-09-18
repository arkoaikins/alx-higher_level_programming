#!/usr/bin/python3

"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
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
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
              .format(sys.argv[4]))
    # retrieve all rows of the states table
    rows = c.fetchall()
    for row in rows:
        print(row)
    # close to clean up resources
    c.close()
    db.close()
