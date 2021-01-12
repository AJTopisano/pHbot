from client import client as client


@client.command()
async def poke(cxt):
    await cxt.send(f'Poke back! {round(client.latency * 1000)}ms')


@client.command()
async def clear(cxt, amount=100):
    await cxt.channel.purge(limit=amount)


@client.command()
async def nyani(ctx):
    await ctx.send('NYNANIIIIIIIII')



