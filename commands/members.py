from loguru import logger
import discord

from ..pHbot import client as client

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