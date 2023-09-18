#!/usr/bin/python3

""" lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys
    # Create a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object to allow the script to execute SQL statements
    c = db.cursor()
    # retrieving  states table
    c.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    # retrieve all rows of the states table
    rows = c.fetchall()
    for row in rows:
        print(row)
    # close to clean up resources
    c.close()
    db.close()
