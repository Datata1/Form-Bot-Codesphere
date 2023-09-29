import discord
from discord.ext import commands

class moderationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('moderationCommands.py is ready!')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f'{count} messages have been deleted.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(selfself, ctx, member: discord.Member, modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title='ok')
        conf_embed.add_field(name ='Kicked',
                             value=f'{member.mention} has been kicked by {ctx.author.mention}.',
                             inline=False)

        await ctx.send(embed=conf_embed)
async def setup(client):
    await client.add_cog(moderationCommands(client))
