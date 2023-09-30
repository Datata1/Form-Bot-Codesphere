import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import json
import asyncio
import re

class embeds(commands.Cog):
    #initialisieren
    def __init__(self, client):
        self.client = client

    def remove_user_from_json(self, username):
        def load_channel_users():
            with open('./channel_users.json', 'r') as f:
                data = json.load(f)
                return data

        def save_channel_users(channel_users):
            with open('./channel_users.json', 'w') as f:
                json.dump(channel_users, f, indent=4)

        channel_user = dict(load_channel_users())

        if username in channel_user['name']:
            channel_user['name'].remove(username)
            save_channel_users(channel_user)
    def load_channel_users(self):
        with open('./channel_users.json', 'r') as f:
            data = json.load(f)
            return data
    def save_channel_users(self, channel_users):
        with open('./channel_users.json', 'w') as f:
            json.dump(channel_users, f, indent=4)

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

        def remove_user_from_json(username):
            channel_user = dict(load_channel_users())
            if username in channel_user['name']:
                channel_user['name'].remove(username)
                save_channel_users(channel_user)

        def is_date(date_string):
            """Prüft, ob der übergebene String das Format YYYY-MM-DD hat.

            Args:
              date_string: Der zu prüfende String.

            Returns:
              True, wenn der String das Format YYYY-MM-DD hat, False sonst.
            """

            date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
            return date_pattern.match(date_string) is not None



        channel_user = dict(load_channel_users())
        print(interaction.user.name)

        if interaction.user.name not in channel_user['name']:

            channel = await interaction.channel.create_thread(name=f'Hackathon #2: Sign up form!',
                                                              type=discord.ChannelType.private_thread)
            channel_user['name'].append(interaction.user.name)
            save_channel_users(channel_user)


            await channel.add_user(interaction.user)
            await channel.send(content='''Hello Challengers! 👋
                It's been a week since the first-ever Codesphere Hackathon kicked off with a round of applause 👏. We are thrilled to announce that we have 17 participants in this exciting challenge!
                
                We understand that the onboarding process might have been a bit confusing since we reached out via email.
                To make things smoother and more interactive, we encourage you to:
                join our Discord community at #💬│support.
                or feel free to add me as a friend and send a private message.
                
                If any participants are interested in discussing potential projects for this challenge or need advice on anything, don't hesitate to reach out to me here on Discord! 😃 
                
                Best regards,
                JD from Codesphere
                ''')
        else:
            await interaction.response.send_message(content='Chanel already exists')


        await interaction.response.send_message(content='Sign Up form initialized in Thread')



async def setup(client):
    await client.add_cog(embeds(client))
