from discord.ext import commands

import ref_functions as rf

from os import getenv
from dotenv import load_dotenv

bot = commands.Bot(command_prefix=".")
load_dotenv()


@bot.command(aliases=['ab'])
async def ability(ctx, *, ability_name: str):
    await ctx.send(rf.get_ability(ability_name.title()))


@bot.command(aliases=['cap'])
async def capability(ctx, *, capability_name: str):
    await ctx.send(rf.get_capability(capability_name.title()))


@bot.command(aliases=['class', 'c'])
async def classes(ctx, *, class_name: str):
    await ctx.send(rf.get_class_mechanic(class_name.title()))


@bot.command(aliases=['e'])
async def edge(ctx, *, edge_name: str):
    await ctx.send(rf.get_edge(edge_name.title()))


@bot.command(aliases=['feat'])
async def feature(ctx, *, feat_name: str):
    await ctx.send(rf.get_feat(feat_name.title()))


@bot.command(aliases=['f'])
async def food(ctx, *, food_name: str):
    await ctx.send(rf.get_food(food_name.title()))


@bot.command(aliases=['hi'])
async def held_item(ctx, *, helditem_name: str):
    await ctx.send(rf.get_held_item(helditem_name.title()))


@bot.command(aliases=['i'])
async def item(ctx, *, item_name: str):
    await ctx.send(rf.get_item(item_name.title()))


@bot.command(aliases=['mv'])
async def move(ctx, *, move_name: str):
    await ctx.send(rf.get_move(move_name.title()))


@bot.command(aliases=['n'])
async def nature(ctx, *, nature_name: str):
    await ctx.send(rf.get_nature(nature_name.title()))


@bot.command(alaises=['pkmne'])
async def pkmnedge(ctx, *, pedge_name: str):
    await ctx.send(rf.get_poke_edge(pedge_name.title()))


@bot.command(aliases=['sts'])
async def status(ctx, *, status_name: str):
    await ctx.send(rf.get_status(status_name.title()))


@bot.command(aliases=['w'])
async def weather(ctx, *, weather_name: str):
    await ctx.send(rf.get_weather(weather_name.title()))


@bot.command(aliases=['pkmnbs'])
async def pkmn_basestats(ctx, *, poke_name):
    await ctx.send(rf.pokemon_info(poke_name.title()))


@bot.command(aliases=['pkmncap'])
async def pkmn_capabilities(ctx, *, poke_name):
    await ctx.send(rf.pokemon_capabilities(poke_name.title()))


@bot.command(aliases=['db'])
async def damage_base(ctx, *, db_num: int):
    await ctx.send(rf.damage_base(db_num))


@bot.command(aliases=['te'])
async def type_effectiveness(ctx, *, pkmn_type: str):
    await ctx.send(rf.get_type_effect(pkmn_type.title()))


@bot.command(aliases=['kw'])
async def keyword(ctx, *, keyword_name: str):
    await ctx.send(rf.get_keyword(keyword_name.title()))

bot.run(getenv('TOKEN'))
