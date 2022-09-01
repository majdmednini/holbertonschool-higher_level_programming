#!/usr/bin/python3
"""
add the state object Louisiana to a db
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_enginea


if __name__ == "__main__":
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    louis = State(name='Louisiana')from sqlalchemy.orm import sessionmaker
    session.add(louis)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.commit()

