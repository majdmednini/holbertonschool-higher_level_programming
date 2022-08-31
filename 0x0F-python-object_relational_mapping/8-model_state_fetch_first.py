#!/usr/bin/python3
"""
print the first state object from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    state1 = session.query(State).order_by(State.id).first()
    if state1 is not None:
        print("{}: {}".format(state1.id, state1.name))
    else:
        print("Nothing")
    session.close()
