from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import discord
import asyncio
from datetime import datetime
import traceback
from consolePrint import console_print
import qrcode



class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='sync', pass_context=True)
    async def sync_tree(self, ctx):
        synced = await self.client.tree.sync()
        await ctx.send(f"{len(synced)} commands synced.")

    @app_commands.command(name='sync', description='Syncs the command tree.')
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def sync(self, inter: discord.Interaction):
        try:
            synced = await inter.client.tree.sync()
            await inter.response.send_message(f"Synced {len(synced)} commands.", ephemeral=True)
            await consolePrint.console_print("tree-sync", f"Command Tree Synced by {inter.user}:{inter.user.id}")
        except Exception as e:
            await inter.response.send_message(f"Error: {traceback.print_exception(e)}", ephemeral=True)
            await consolePrint.console_print("tree-sync-error", f"Command Tree Synced by {inter.user}:{inter.user.id} | {e}")

    @sync.error
    async def sync_error(self, interaction, error):
        await interaction.response.send_message(error, ephemeral=True)


async def setup(client):
    await client.add_cog(Commands(client))
