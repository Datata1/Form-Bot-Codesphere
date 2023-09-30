import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import json

class embeds(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Embeds.py is ready!')

    @app_commands.command(name='signup', description='Create your Sign up Form for the HAckthon #2')
    async def signup(self, interaction: discord.Interaction):
        def load_channel_users():
            with open('./channel_users.json', 'r') as f:
                data = json.load(f)
                return data

        def save_channel_users(channel_users):
            with open('./channel_users.json', 'w') as f:
                json.dump(channel_users, f, indent=4)

        channel_user = dict(load_channel_users())

        print(interaction.user.name)

        if interaction.user.name not in channel_user['name']:
            print('hi)')
            channel = await interaction.channel.create_thread(name=f'Hackthon signup',
                                                              type=discord.ChannelType.private_thread)
            channel_user['name'].append(interaction.user.name)
            save_channel_users(channel_user)

            await channel.add_user(interaction.user)
        else:
            await interaction.response.send_message(content='Chanel already exists')


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
