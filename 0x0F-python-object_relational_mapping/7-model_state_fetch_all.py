#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
import warnings
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    us = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    p = 'mysql+mysqldb://{}:{}@localhost/{}'.format(us, ps, db)
    engine = create_engine(p, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sn = sessionmaker(bind=engine)
    sn = sn()
    for state in sn.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
    sn.close()
