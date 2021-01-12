import os
from loguru import logger
from dotenv import load_dotenv

from pHbot import client as client
from commands.members import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
    logger.info("Starting client")
    client.run(TOKEN)
