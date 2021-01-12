from loguru import logger
from client import client as client


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    logger.debug(f"received \"{message.content}\" from {message.author.name}")

    await client.process_commands(message)
