import discord
from discord.ext import commands
import random
from loguru import logger


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    logger.info("PyBot is ready")


@client.command()
async def poke(cxt):
    await cxt.send(f'Poke back! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(cxt, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
    await cxt.send(f'Question: {question}\nAnswer : {random.choice(responses)}')


@client.command()
async def clear(cxt, amount=100):
    await cxt.channel.purge(limit=amount)


@client.command()
async def nyani(ctx):
    await ctx.send('NYNANIIIIIIIII')

