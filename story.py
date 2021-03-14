from discord.ext import commands


# EVENT LISTENER FOR PRINTING OUT THE GAME STORY INTRODUCTION.
class Story(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def intro(self, ctx):
        """Prints the story introduction."""
        await ctx.send(f"{ctx.message.author.mention}\n```Welcome to \n"
                       ' #####                                       ######  ######   #####  \n'
                       '#     #   ##   #####  ####  #    #   ##      #     # #     # #     # \n'
                       '#        #  #    #   #    # #    #  #  #     #     # #     # #       \n'
                       '#  #### #    #   #   #      ###### #    #    ######  ######  #  #### \n'
                       '#     # ######   #   #      #    # ######    #   #   #       #     # \n'
                       '#     # #    #   #   #    # #    # #    #    #    #  #       #     # \n'
                       ' #####  #    #   #    ####  #    # #    #    #     # #        #####  ```')
        await ctx.send('```In a world, where dangerous creatures roam the land, you are an aspiring summoner. Once a '
                       'day, you have the ability to cast a powerful summoning spell to call forth a poor soul that '
                       'got hit by a truck and passed away in their past life. The summoned servant has no memories of '
                       'their past life and is willing to assist you in making the world a safer place. Woohoo! Have '
                       'them slay monsters to hone their skills. Strive to become the most powerful summoner with the '
                       'strongest servants.```')


def setup(bot):
    bot.add_cog(Story(bot))
