import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio

os.getcwd()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot_status = cycle(['Hackathon #1', '/signup'])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Activity(name=next(bot_status), type=5))

@client.event
async def on_ready():
    await client.tree.sync()
    print('Bot is online')
    change_status.start()


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with client:
        await load()
        await client.start('insert token')


asyncio.run(main())

