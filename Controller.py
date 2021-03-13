import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import character_creation
from discord.ext.commands import CommandNotFound

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

client = discord.Client()
bot.remove_command("help")


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.command(name='hello')
async def test(ctx):
    em = discord.Embed(title="Hello", description="Please fuck off")
    await ctx.send(embed=em)


@bot.command(name='slap')
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = "and ".join(x.name for x in members)
    await ctx.send('I just slapped {} for {}'.format(slapped, reason))


@bot.command(name='createCharacter')
async def create(ctx):
    # if user.character == already exists:
    #      tell user that they already have a main character
    # else: do the stuff below
    new_character = character_creation.main()
    em = discord.Embed(title="\U00002694 Create Character \U00002694",
                       description=f"User {ctx.message.author.mention} created a new character")
    em.add_field(name="Character Bio", value=f"{new_character}")
    await ctx.send(embed=em)


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help Menu", description="\U0001F44B Hi User! Looks like you called for help\nUse $help "
                                                      "<command> for additional info on each command")
    em.add_field(name="\U0001F5FA Story:", value="location\n goto\n returnhome")
    em.add_field(name="\U0001F392 Shop:", value="buy\n sell")

    await ctx.send(embed=em)


@help.command()
async def location(ctx):
    em = discord.Embed(title="\U0001F3D5 Location", description="Fetches your current location", color=ctx.author.color)
    em.add_field(name="**Syntax**", value="$location")
    await ctx.send(embed=em)


@help.command()
async def goto(ctx):
    em = discord.Embed(title="\U0001F6B6 Go To", description="Takes you to the entered location",
                       color=ctx.author.color)
    em.add_field(name="**Syntax**", value="$goto [location name]")
    await ctx.send(embed=em)


@help.command()
async def returnhome(ctx):
    em = discord.Embed(title="\U0001F3DA Return Home", description="Takes you back to town", color=ctx.author.color)
    em.add_field(name="**Syntax**", value="$returnhome")
    await ctx.send(embed=em)


@help.command()
async def buy(ctx):
    em = discord.Embed(title="\U0001F4B0 Buy Item", description="Buys your desired item from the store",
                       color=ctx.author.color)
    em.add_field(name="**Syntax**", value="$buy [item name]")
    await ctx.send(embed=em)


@help.command()
async def sell(ctx):
    em = discord.Embed(title="\U0001F4B0 Sell Item", description="Sells your desired item in the store",
                       color=ctx.author.color)
    em.add_field(name="**Syntax**", value="$sell [item name]")
    await ctx.send(embed=em)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        em = discord.Embed(title="\U00002620 Bad Command \U00002620", description="That's not a valid command, idiot.")
        await ctx.send(embed=em)


bot.run(DISCORD_TOKEN)
