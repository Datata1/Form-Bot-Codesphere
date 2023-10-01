import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import json
import asyncio
import re


class inputmodal(discord.ui.Modal, title='personal information'):
    email = discord.ui.TextInput(label='email adress', placeholder='example@example.com', required=True,
                                 style=discord.TextStyle.short)
    bdate = discord.ui.TextInput(label='birthdate', placeholder='mm.dd.yyyy', required=True,
                                 style=discord.TextStyle.short)

    class menubutton(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label='Submit', style=discord.ButtonStyle.green)
        async def test(self, interaction: discord.Interaction, Button: discord.ui.Button):
            def load_channel_users():
                with open('./participants.json', 'r') as f:
                    data = json.load(f)
                    return data

            def save_channel_users(channel_users):
                with open('./participants.json', 'w') as f:
                    json.dump(channel_users, f, indent=4)

            channel_user = dict(load_channel_users())
            print(channel_user)
            name = interaction.user.name
            print(name)

            print(data)
            channel_user[name] = [data[0], data[1]]
            save_channel_users(channel_user)

            channel = await interaction.channel.guild.fetch_channel('1157012029920514118') #this should be the Channel of the supporter

            await channel.send(embed=embed_message)

            await interaction.response.send_message(content='Your submission was successful', ephemeral=True)

    async def on_submit(self, interaction: discord.Interaction):
        global dater

        dater = [self.email.value, self.bdate.value]

        global embed_message

        embed_message = discord.Embed(title='Hackathon',
                                      description='this is lit!',
                                      color=discord.Color.random(),
                                      url='https://codesphere.com/')
        embed_message.set_author(name=f'Participant {interaction.user.name}',
                                 icon_url=interaction.user.avatar)
        embed_message.add_field(name='Email adress',
                                value=f'{dater[0]}',
                                inline=True)
        embed_message.add_field(name='date of birth',
                                value=f'{dater[1]}',
                                inline=True)
        embed_message.add_field(name='text',
                                value='bliblablubb',
                                inline=False)
        embed_message.set_thumbnail(url=interaction.guild.icon)
        # embed_message.set_image(url=interaction.guild.icon)
        embed_message.add_field(name='Confirmation of terms and Conditions',
                                value='[Termans and Conditions](https://www.ihk.de/hamburg/produktmarken/beratung-service/recht-und-steuern/wirtschaftsrecht/vertragsrecht/allgemeine-geschaeftsbedingungen-1156958#:~:text=Allgemeine%20Gesch%C3%A4ftsbedingungen%20(AGB)%20sind%20f%C3%BCr,1%20BGB)')
        embed_message.set_footer(text='LSBNNLASNDFALDKN',

                                 icon_url=interaction.user.avatar)

        global data

        data = [dater[0], dater[1]]
        print(data)

        active_threads = await interaction.guild.active_threads()
        print(active_threads)
        userthread = f'Hackathon #2: Sign up form for {interaction.user.name}'
        active_threads_dict = {}

        for thread in active_threads:
            thread_name = thread.name
            thread_id = thread.id
            active_threads_dict[thread_name] = thread_id

        # Print the resulting dictionar
        print(active_threads_dict)

        thisThread = await interaction.channel.guild.fetch_channel(f'{active_threads_dict[userthread]}')

        print(thisThread)

        await thisThread.send(embed=embed_message, view=inputmodal.menubutton())
        await interaction.response.send_message(content='yes', ephemeral=True)


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

        channel_user = dict(load_channel_users())

        print(interaction.user.name)
        names = interaction.user.name
        if interaction.user.name not in channel_user['name']:

            channel = await interaction.channel.create_thread(name=f'Hackathon #2: Sign up form for {names}',
                                                              type=discord.ChannelType.private_thread)
            print(channel)
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

        await interaction.response.send_modal(inputmodal())


class form(commands.Cog):
    #initialisieren
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('forms_hackthon#2.py is ready!')

    @app_commands.command(name='hackathon', description='Sign up for the hackathon #2')
    async def form(self, interaction: discord.Interaction):

        await interaction.response.send_modal(inputmodal())


async def setup(client):
    await client.add_cog(embeds(client))
