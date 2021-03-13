# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import random
import typing

import discord
from discord.ext import commands

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# ADDS SPECIFIC COMMAND TO INITIALIZE BOT ACTIONS
bot = commands.Bot(command_prefix='$')


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.command()
async def test(ctx, arg):
    if arg == "hello":
        await ctx.send("hey fuck you")


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = "and ".join(x.name for x in members)
    await ctx.send('I just slapped {} for {}'.format(slapped, reason))


client = discord.Client()

bot.run(DISCORD_TOKEN)
