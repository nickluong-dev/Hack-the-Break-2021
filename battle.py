import discord
from discord.ext import commands
from random import choice
import character_classes


AVAILABLE_MONSTERS = [character_classes.Goblin,
                      character_classes.Zombie,
                      character_classes.Werewolf,
                      character_classes.Vampire]


class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def encounter(self, ctx):
        """Generates a random encounter."""
        monster = choice(AVAILABLE_MONSTERS)()

        await ctx.send(f'```As you are traversing the dark dungeon, a terrifying {monster.__class__.__name__} leaps '
                       f'out at you!```')

        em = discord.Embed(title="Monster Stats",
                           description=f"{monster.__class__.__name__}'s Stats")
        em.add_field(name="HP: ", value=monster.hp)
        em.add_field(name="MP: ", value=monster.mp)
        em.add_field(name="Attack: ", value=monster.attack)
        em.add_field(name="Magic Attack: ", value=monster.magic_attack)
        em.add_field(name="Defense: ", value=monster.defense)
        em.add_field(name="Resistance: ", value=monster.resistance)
        em.add_field(name="Total Stats: ", value=(monster.hp + monster.mp + monster.attack + monster.magic_attack +
                                                  monster.defense + monster.resistance))
        em.add_field(name="Description: ", value=monster.description)
        await ctx.send(embed=em)
        await ctx.send(f'```What will you do? (FIGHT, FLEE)```')

    @commands.command()
    async def fight(self, ctx):
        """One round of a fight against a monster."""
        # get character class from database and calculate monster damage using attack
        # calculate monster hp and end battle if <= 0
        # calculate player damage using monster attack
        # calculate monster hp and end battle if <= 0
        # save stats
        # show battle options again if battle is not over
        await ctx.send(f'```Everybody was kung fu fighting\nThose cats were fast as lightning```')

    @commands.command()
    async def flee(self, ctx):
        """Flee like the coward that you are."""
        await ctx.send(f'```Got out of there quicker than the Toronto Maple Leafs in the play-offs.```')


def setup(bot):
    bot.add_cog(Battle(bot))
