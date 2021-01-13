import discord
from discord.ext import commands
from loguru import logger
from client import client as client
import random

moves = ['rock', 'paper', 'scissors']


@client.command()
async def rps(ctx, move):
    global moves

    x = str(move).lower()
    k = random.choice(moves)

    if x == k:
        await ctx.send(k.capitalize() + ", it's a tie.")

    if x == 'rock' and k == 'paper':
        await ctx.send(k.capitalize() + ", I won.")

    if x == 'rock' and k == 'scissors':
        await ctx.send(k.capitalize() + ", You won.")

    if x == 'paper' and k == 'rock':
        await ctx.send(k.capitalize() + ", You won.")

    if x == 'paper' and k == 'scissors':
        await ctx.send(k.capitalize() + ", I won.")

    if x == 'scissors' and k == 'paper':
        await ctx.send(k.capitalize() + ", You won.")

    if x == 'scissors' and k == 'rock':
        await ctx.send(k.capitalize() + ", I won.")

    if x not in moves:
        await ctx.send("Enter a valid input i.e(rock, paper, scissors)")
