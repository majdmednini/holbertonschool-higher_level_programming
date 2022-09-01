#!/usr/bin/python3
"""
add the state object Louisiana to a db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":

    user = argv[1]
    pas = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, pas, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
