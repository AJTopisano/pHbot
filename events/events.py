from loguru import logger
from client import client as client


@client.event
async def on_ready():
    logger.info("PyBot is ready")