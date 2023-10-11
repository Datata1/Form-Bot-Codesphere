import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import json



class inputmodal(discord.ui.Modal, title='personal information'):
    # here you can set up the data the user has to provide in order to sign up for the hackathon
    email = discord.ui.TextInput(label='email adress', placeholder='example@example.com', required=True, style=discord.TextStyle.short)

    class menubutton(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        # This creates the green Submit button
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
            channel_user[name] = data[0]
            save_channel_users(channel_user)

            # the channel where the bot is sending the form
            channel = await interaction.channel.guild.fetch_channel(1161348630213578914)

            print(interaction.channel)

            await channel.send(embed=embed_message)

            await interaction.response.send_message(content='Your submission was successful', ephemeral=True)
    async def on_submit(self, interaction: discord.Interaction):
        global dater

        dater = [self.email.value]

        global embed_message

        # Here you can change the appearence of the form (embed)
        embed_message = discord.Embed(title='Hackathon',
                                      description='this is lit!',
                                      color=discord.Color.random(),
                                      url='https://codesphere.com/')
        embed_message.set_author(name=f'Participant {interaction.user.name}',
                                 icon_url=interaction.user.avatar)
        embed_message.add_field(name='Email adress',
                                value=f'{self.email.value}',
                                inline=True)
        embed_message.add_field(name='add other data',
                                value=f'anything you like',
                                inline=True)
        embed_message.add_field(name='text',
                                value='here you can write the stuff down you need to mention',
                                inline=False)
        embed_message.set_thumbnail(url=interaction.guild.icon)
        # embed_message.set_image(url=interaction.guild.icon)
        embed_message.add_field(name='Confirmation of terms and Conditions',
                                value='[Termans and Conditions](https://www.ihk.de/hamburg/produktmarken/beratung-service/recht-und-steuern/wirtschaftsrecht/vertragsrecht/allgemeine-geschaeftsbedingungen-1156958#:~:text=Allgemeine%20Gesch%C3%A4ftsbedingungen%20(AGB)%20sind%20f%C3%BCr,1%20BGB)')
        embed_message.set_footer(text='by clicking on the submit button you accept the Terms and Conditions',

                                 icon_url=interaction.user.avatar)

        global data

        data = [dater[0], dater[1]]
        print(data)

        # This command creates the complete form and send ir back to the user
        await interaction.response.send_message(embed=embed_message, view=inputmodal.menubutton(), ephemeral=True)

        # ephemeral means that only the user can see the generated messages from the Bot

class form(commands.Cog):
    #initialisieren
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('forms_hackthon#2.py is ready!')

    @app_commands.command(name='akk', description='Sign up for the hackathon #2')
    async def form(self, interaction: discord.Interaction):
        # This command triggers the modal, where the user inputs the data
        await interaction.response.send_modal(inputmodal())



async def setup(client):
    await client.add_cog(form(client))