import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction


class embeds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Embeds.py is ready!')

    @app_commands.command(name='signup', description='Create your Sign up Form for the HAckthon #2')
    async def signup(self, interaction: discord.Interaction):
        embed_message = discord.Embed(title='Hackathon',
                                      description='this is lit!',
                                      color=discord.Color.random())
        embed_message.set_author(name=f'Requested by {interaction.user.name}',
                                 icon_url=interaction.user.avatar)
        embed_message.add_field(name='Field name',
                                value='Value',
                                inline=True)
        embed_message.set_thumbnail(url=interaction.guild.icon)
        embed_message.set_image(url=interaction.guild.icon)
        embed_message.set_footer(text='footer', icon_url=interaction.user.avatar)

        await interaction.response.send_message(embed=embed_message)
async def setup(client):
    await client.add_cog(embeds(client))
