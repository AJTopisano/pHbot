import os
from loguru import logger
from dotenv import load_dotenv
from sqlalchemy import create_engine


class Database:
    def __init__(self):
        load_dotenv()
        database_url = os.getenv('DATABASE_URL')
        self.engine = create_engine(database_url)
        # Database successfully connected
        logger.info(f"Connected to database {database_url}")

    def create_table(self, table):
        table.create(self.engine)


if __name__ == '__main__':
    from sqlalchemy import Table, Column, Integer, String, MetaData

    meta = MetaData()

    project = Table(
        'project', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('description', String),
    )

    db = Database()
    db.create_table(project)
