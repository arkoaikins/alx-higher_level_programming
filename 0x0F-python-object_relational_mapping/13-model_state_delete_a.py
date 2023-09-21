#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
