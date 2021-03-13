from discord.ext import commands


# EVENT LISTENER FOR PRINTING OUT THE GAME STORY INTRODUCTION.
class Story(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def intro(self, ctx):
        """Prints the story introduction."""
        await ctx.send('Welcome to Gatcha RPG!')


def setup(bot):
    bot.add_cog(Story(bot))
