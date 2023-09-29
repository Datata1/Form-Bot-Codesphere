import discord
from discord import app_commands
from discord.ext import commands
# Bot-Token
TOKEN = 'insert token'

# Intents erstellen
intents = discord.Intents.default()

# Intents aktivieren
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

# Bot-Client erstellen
client = commands.Bot(intents=intents, command_prefix='/')


# Command-Tree erstellen
tree = app_commands.CommandTree(client)

# On-Ready-Event
@client.event
async def on_ready():
  for server in client.guilds:
    await client.tree.sync(guild=discord.Object(id=1148327198537818182))
    print("Bot ist online!")

# Slash-Command
@client.command(name = "signup", description = "hackathon") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
 await interaction.response.send_message("Willkommen zum Anmeldeformular!")

# Bot starten
client.run(TOKEN)