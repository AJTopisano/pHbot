import psycopg2
import urllib.parse as urlparse
import os
from loguru import logger


def connect_db():
    """
    Connect to postgres database hosted on Heroku.

    environment variable DATABASE_URL should be added to .env or env variables on Heroku
    the database url can be found by `heroku config:get DATABASE_URL -a phbot8` on CLI
    """
    db_url = os.getenv('DATABASE_URL')
    url = urlparse.urlparse(db_url)
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port

    # Attempt to create connection
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        # Database successfully connected
        logger.info(f"Connected to database {dbname} on port {port}, hosted by {host}")
        return conn

    except psycopg2.OperationalError:
        # Connection failed
        logger.critical(f"Unable to connect to database {dbname} on port {port}, hosted by {host}")


if __name__ == '__main__':
    """Test if a valid connection can be made"""
    from dotenv import load_dotenv
    load_dotenv()
    connection = connect_db()
