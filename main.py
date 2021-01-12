import os
from loguru import logger
from dotenv import load_dotenv

from client import client as client
from commands.members import *
from commands.other import *
from commands.eight_ball import *
from events.events import *


load_dotenv()
TOKEN = os.environ('DISCORD_TOKEN')

if __name__ == '__main__':
    logger.info("Starting client")
    client.run(TOKEN)
