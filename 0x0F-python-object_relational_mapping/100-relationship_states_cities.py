#!/usr/bin/python3
""" relations """
import sys
from relationship_state import Base, State
from relationship_city import City
import warnings
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    usr = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, ps, db, pool_pre_ping=True))

    Base.metadata.create_all(engine)
    sn = sessionmaker(bind=engine)
    sn = sn()
    cl = State(name='California')
    cl.cities.append(City(name="San Francisco"))
    sn.add(cl)
    sn.commit()
    sn.close()
