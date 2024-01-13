#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
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
    result = (
            sn.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(State.id, City.id)
            .all()
            )
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    sn.close()
