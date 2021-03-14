import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import character_creation
from discord.ext.commands import CommandNotFound , Bot
from discord.ext.commands import Bot

import character_classes

# THE LIST OF EXTENSIONS THAT ARE LOADED WHEN THE BOT STARTS UP
startup_extensions = ["story"]

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
    await bot.change_presence(activity=discord.Game('Fortnite'))


@bot.command()
async def load(ctx, extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


@bot.command()
async def unload(ctx, extension_name: str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))


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


@bot.command(name='selectClass')
async def select_class(ctx, chosen_class='none'):
    altered_chosen = chosen_class.title()
    spec_list = ['Warrior', 'Mage', 'Thief', 'Priest']
    if altered_chosen in spec_list:
        # new_spec = character_classes.Player.
        await ctx.send(f"good class: {altered_chosen} with specs: ")
    else:
        await ctx.send(f"class does not exist: {chosen_class}")

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


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(DISCORD_TOKEN)
