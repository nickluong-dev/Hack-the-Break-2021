import discord
import character_classes
from discord.ext import commands

AVAILABLE_CLASSES = {"\U0001F6E1": character_classes.Warrior,
                     "\U0001FA84": character_classes.Mage,
                     "\U0001F94A": character_classes.Brawler,
                     "\U0001F489": character_classes.Priest,
                     "\U0001FAA6": character_classes.DarkKnight,
                     "\U0001F5E1": character_classes.Thief}

AVAILABLE_REACTIONS = [key for key in AVAILABLE_CLASSES.keys()]
bot = commands.Bot(command_prefix='$')
client = discord.Client()

user_reacted = set()
user_chosen_class = {}


def object_to_dictionary(user_class_object):
    player_dict = {'class': user_class_object.__class__.__name__,
                   'hp': user_class_object.hp,
                   'mp': user_class_object.mp,
                   'attack': user_class_object.attack,
                   'magic_attack': user_class_object.magic_attack,
                   'defense': user_class_object.defense,
                   'resistance': user_class_object.resistance,
                   'description': user_class_object.description,
                   'rarity': user_class_object.rarity,
                   'exp': user_class_object.exp}
    return player_dict


def users_collection_of_classes(user_classes):
    collection = dict()
    for key in user_classes.keys():
        collection[key] = object_to_dictionary(user_classes[key])

    return collection


class user_controller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = None

    user_reacted = set()

    @commands.command()
    async def start(self, ctx):
        em = discord.Embed(title="Create Character",
                           description=f"Choose a class for your first character {ctx.message.author.mention}.")
        em.add_field(name="Warrior", value="\U0001F6E1")
        em.add_field(name="Mage", value="\U0001FA84")
        em.add_field(name="Brawler", value="\U0001F94A")
        em.add_field(name="Priest", value="\U0001F489")
        em.add_field(name="DarkKnight", value="\U0001FAA6")
        em.add_field(name="Thief", value="\U0001F5E1")
        msg = await ctx.send(embed=em)
        self.message = msg
        await msg.add_reaction("\U0001F6E1")
        await msg.add_reaction("\U0001FA84")
        await msg.add_reaction("\U0001F94A")
        await msg.add_reaction("\U0001F489")
        await msg.add_reaction("\U0001FAA6")
        await msg.add_reaction("\U0001F5E1")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        user = await self.bot.fetch_user(payload.user_id)
        emoji = payload.emoji

        print(user_reacted)
        print(payload.user_id)

        if self.message.id == payload.message_id and payload.user_id not in user_reacted and payload.user_id != 820355672587108422:
            user_reacted.add(payload.user_id)
            user_chosen_class[self.message.id] = AVAILABLE_CLASSES[emoji.name]()
            print(self.message.id)
            em = discord.Embed(title="Your Stats",
                               description=f"{payload.member.name}'s {user_chosen_class[self.message.id].get_classname()} "
                                           f"Stats")
            em.add_field(name="HP: ", value=user_chosen_class[self.message.id].get_hp())
            em.add_field(name="MP: ", value=user_chosen_class[self.message.id].get_mp())
            em.add_field(name="Attack: ", value=user_chosen_class[self.message.id].get_attack())
            em.add_field(name="Magic Attack: ", value=user_chosen_class[self.message.id].get_magic_attack())
            em.add_field(name="Defense: ", value=user_chosen_class[self.message.id].get_defense())
            em.add_field(name="Resistance: ", value=user_chosen_class[self.message.id].get_resistance())
            em.add_field(name="Description: ", value=user_chosen_class[self.message.id].get_description(), inline=False)
            em.add_field(name="Rarity: ", value=user_chosen_class[self.message.id].get_rarity(), inline=False)
            await channel.send(embed=em)


    @commands.command()
    async def stats(self, ctx):
        collection = users_collection_of_classes(user_chosen_class)

        for user, char_classes in collection.items():
            await ctx.send(char_classes['hp'])
            em = discord.Embed(title="Your Stats",
                               description=f"{ctx.message.author.mention}'s {char_classes['class']}")
            em.add_field(name="HP: ", value=char_classes['hp'])
            em.add_field(name="MP: ", value=char_classes['mp'])
            em.add_field(name="Attack: ", value=char_classes['attack'])
            em.add_field(name="Magic Attack: ", value=char_classes['magic_attack'])
            em.add_field(name="Defense: ", value=char_classes['defense'])
            em.add_field(name="Resistance: ", value=char_classes['resistance'])
            em.add_field(name="Description: ", value=char_classes['description'], inline=False)
            em.add_field(name="Rarity: ", value=char_classes['rarity']['Rarity'], inline=False)
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(user_controller(bot))
