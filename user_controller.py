import character_classes
import random
import Controller
from discord.ext import commands

available_user_characters = []
AVAILABLE_CLASSES = [character_classes.Warrior,
                     character_classes.Mage,
                     character_classes.Brawler,
                     character_classes.Priest,
                     character_classes.DarkKnight,
                     character_classes.Thief]


class user_controller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def get_stats(self, ctx):
    #     await ctx.send(test_print())


def setup(bot):
    bot.add_cog(user_controller(bot))
