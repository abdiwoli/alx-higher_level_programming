#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, text


if __name__ == "__main__":
    us = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    p = 'mysql+mysqldb://{}:{}@localhost/{}'.format(us, ps, db)
    engine = create_engine(p, pool_pre_ping=True)

    q = text("SELECT * FROM states ORDER BY id;")

    result = engine.execute(q)

    for i, v in result:
        print(f"{i}: {v}")
