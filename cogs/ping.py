import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping.py is ready!')

    @app_commands.command(name='ping', description='latency of the bot')
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(bot_latency)
async def setup(client):
    await client.add_cog(Ping(client))
