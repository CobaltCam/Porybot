import discord
from discord.ext import commands

import ref_functions as rf
import pkmndice
import hitpoint_counter as hp
# from os import getenv
# from dotenv import load_dotenv

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
# load_dotenv()
hp = hp.HitPointTracker()

# Commands for the reference function of Porybot, each tied to one of the functions in ref_functions. These commands
# call the associated function and then send the formatted string to discord.


@bot.command(aliases=['ab', 'Ability'])
async def ability(ctx,* , ability_name: str):
    await ctx.send(rf.get_ability(ability_name.title()))


@bot.command(aliases=['cap', 'Capability'])
async def capability(ctx, *, capability_name: str):
    await ctx.send(rf.get_capability(capability_name.title()))


@bot.command(aliases=['cl', 'class', 'Class'])
async def classes(ctx, *, class_name: str):
    await ctx.send(rf.get_class_mechanic(class_name.title()))


@bot.command(aliases=['e', 'ed', 'Edge'])
async def edge(ctx, *, edge_name: str):
    await ctx.send(rf.get_edge(edge_name.title()))


@bot.command(aliases=['f', 'feat', 'Feat', 'Feature'])
async def feature(ctx, *, feature_name: str):
    await ctx.send(rf.get_feat(feature_name.title()))


@bot.command(aliases=['Food'])
async def food(ctx, *, food_name: str):
    await ctx.send(rf.get_food(food_name.title()))


@bot.command(aliases=['hitem', 'heldi', 'Held_Item'])
async def held_item(ctx, *, held_item_name: str):
    await ctx.send(rf.get_held_item(held_item_name.title()))


@bot.command(aliases=['i', 'Item'])
async def item(ctx, *, item_name: str):
    await ctx.send(rf.get_item(item_name.title()))


@bot.command(aliases=['mv', 'Move'])
async def move(ctx, *, move_name: str):
    await ctx.send(rf.get_move(move_name.title()))


@bot.command(aliases=['nat', 'Nature'])
async def nature(ctx, *, nature_name: str):
    await ctx.send(rf.get_nature(nature_name.title()))


@bot.command(aliases=['pedge', 'Pokeedge', 'poke-edge', 'Poke-edge'])
async def pokeedge(ctx, *, pokeedge_name: str):
    await ctx.send(rf.get_poke_edge(pokeedge_name.title()))


@bot.command(alaises=['s', 'statuses', 'Status'])
async def status(ctx, *, status_name: str):
    await ctx.send(rf.get_status(status_name.title()))


@bot.command(aliases=['w', 'Weather'])
async def weather(ctx, *, weather_name: str):
    await ctx.send(rf.get_weather(weather_name.title()))


@bot.command(aliases=['pokecap', 'Pokemon-Capabilities', 'pokemon-capabilities'])
async def pokemon_capabilities(ctx, *, pokemon_name: str):
    await ctx.send(rf.pokemon_capabilities(pokemon_name.title()))


@bot.command(aliases=['base stats', 'bs', 'Base-Stats'])
async def base_stats(ctx, *, pokemon_name: str):
    await ctx.send(rf.pokemon_info(pokemon_name.title()))


@bot.command(aliases=['db', 'damage-base', 'Damage-Base'])
async def damage_base(ctx, *, d_base: int):
    await ctx.send(rf.damage_base(d_base))


@bot.command(aliases=['te', 'Type-Effectiveness', 'type-effectiveness', 'type'])
async def type_effectiveness(ctx, *, type: str):
    await ctx.send(rf.get_type_effect(type.title()))


@bot.command(aliases=['kw', 'Keyword'])
async def keyword(ctx, *, kw: str):
    await ctx.send(rf.get_keyword(kw.title()))

# -------------------------------------------------DICE COMMANDS------------------------------------------------------ #
@bot.command(aliases=['r'])
async def roll(ctx, *, dice):
    await ctx.reply(pkmndice.manual_roll(dice))


@bot.command(aliases=['rdb', 'damageroll'])
async def roll_damage(ctx, damagebase: int):
    await ctx.reply(pkmndice.rolled_damage(damagebase))

#--------------------------------------------------HitpointCounter-----------------------------------------------------#

@bot.command()
async def reset(ctx):
    await ctx.send(hp.encounter_start())


@bot.command()
async def add(ctx, com_name: str, hitpoints: int):
    await ctx.send(hp.add_combatant(com_name, hitpoints))


@bot.command()
async def check(ctx, combatant: str):
    await ctx.send(hp.check_combatant(combatant))


@bot.command()
async def remove(ctx, combatant: str):
    await ctx.send(hp.remove_combatant(combatant))

@bot.command()
async def update(ctx, combatant: str, value: int):
    await ctx.send(hp.update_hitpoints(combatant, value))

@bot.command()
async def list(ctx):
    await ctx.send(hp.list_hitpoints())


bot.run('TOKEN')
