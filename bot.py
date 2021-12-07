import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions, is_owner
import os
import config

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!help'))


@bot.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} has been loaded!')

@bot.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} has been unloaded!')

@bot.command()
@has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog {extension} has been reloaded!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded {filename[:-3]}")
    else:
        print(f'Unable to load {filename[:-3]}')


bot.run(config.token)