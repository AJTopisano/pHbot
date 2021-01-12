import discord
from discord.ext import commands




intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='$', intents=intents)

