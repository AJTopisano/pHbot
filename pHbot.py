import discord
from discord.ext import commands
import random

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("PyBot is ready")


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
async def kick(cxt, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(cxt, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await cxt.send(f'Banned {member.mention}')


@client.command()
async def unban(cxt, *, member):
    banned_users = await cxt.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await cxt.guild.unban(user)
            await cxt.send(f'Unbanned {user.name}#{user.discriminator}')


@client.command()
async def nyani(ctx):
    await ctx.send('NYNANIIIIIIIII')


client.run('Nzk4MTk5Nzc2MTAwNjE0MTQ1.X_xjeA.WvFezzQBVmEMpu6GifNDf6ZQs-0')
