import datetime

import sqlalchemy as sa
from sqlalchemy import event

from sqlalchemy.orm import sessionmaker

from app.models import User

engine = sa.create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres', echo=False)
session = sessionmaker(bind=engine)()

tables = ['listofgrades',
          'class',
          'lesson',
          'grade',
          'pupil',
          'teacher',
          'user']

for table in tables:
    session.execute("TRUNCATE %s CASCADE" % table)
session.commit()

if __name__ == "__main__":
    with engine.connect() as conn:
        result = session.execute("SELECT 1")
        print(result)
        print(result.fetchone())
