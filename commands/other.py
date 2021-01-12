from loguru import logger
from client import client as client


@client.command()
async def poke(cxt):
    logger.info(f'Poke back! {round(client.latency * 1000)}ms')
    await cxt.send(f'Poke back! {round(client.latency * 1000)}ms')


@client.command()
async def clear(cxt, amount=100):
    await cxt.channel.purge(limit=amount)


@client.command()
async def nyani(ctx):
    await ctx.send('NYNANIIIIIIIII')


@client.command()
async def help(cxt):
    await cxt.send('Do it yourself')
