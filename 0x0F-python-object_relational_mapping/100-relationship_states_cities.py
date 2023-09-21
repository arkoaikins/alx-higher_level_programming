#!/usr/bin/python3
"""
script that creates the State “California” with the City
“San Francisco” from the database
"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cre_State = State(name='California')
    cre_City = City(name='San Francisco')
    cre_State.cities.append(cre_City)

    session.add(cre_State)
    session.add(cre_City)
    session.commit()
    session.close()
