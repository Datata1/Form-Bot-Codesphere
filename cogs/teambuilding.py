import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction



class Team(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('teambuilding.py is ready!')

    @app_commands.command(name='teamup', description='Create you Team with the maximum of 3 people')
    async def team(self, interaction: discord.Interaction, member: discord.Member=None):
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member

        avatar_embed = discord.Embed(title=f"")






async def setup(client):
    await client.add_cog(Team(client))