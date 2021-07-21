import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

client=commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is Up and Running.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {user.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {user.mention}')

@client.command()
async def warn(ctx, member : discord.Member, *, reason=None):
    await member.warn(reason=reason)
    await ctx.send(f'Warned {user.mention}')

@client.command()
async def unban(ctx, *,member):
    banned_users=await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user=ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run(str(os.getenv("TOKEN")))
