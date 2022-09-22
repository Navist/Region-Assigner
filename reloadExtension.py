from modulefinder import Module
from typing import Any
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from importlib import reload
import asyncio
import consolePrint

class reloadExtension(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name='reload_module', description="Reloads a module that is outside the normal scope of bot.")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def reload_module(self, inter: discord.Interaction, module_name: str):
        module_name = reload(eval(module_name))

        await consolePrint.console_print("module-reload", f"{module_name}")
        await inter.response.send_message(f"{module_name} has been reloaded.", ephemeral=True)

    @reload_module.error
    async def reload_module_error(self, inter, error):
        await inter.response.send_message(error, ephemeral=True)

    @app_commands.command(name='re', description='Reloads an extension.')
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def reloadEx(self, interaction: discord.Interaction, extension: str):
        try:
            await self.client.reload_extension(extension)
        except Exception as error:
            await interaction.response.send_message(error, ephemeral=True)
            await consolePrint.console_print("module-error", f"{extension}\n{error}")
            return
        await consolePrint.console_print("module-reload", f"{extension}")
        await interaction.response.send_message(f"Reloaded {extension}", ephemeral=True)


    @app_commands.command(name='le', description='Loads an extension.')
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(extension="Which extension would you like to load?")
    @app_commands.checks.has_permissions(administrator=True)
    async def loadEx(self, interaction: discord.Interaction, extension: str):
        await consolePrint.console_print("module-load", f"{extension}")
        try:
            await self.client.load_extension(extension)
        except Exception as error:
            await interaction.response.send_message(error, ephemeral=True)
            await consolePrint.console_print("module-error", f"{extension}\n{error}")
            return

        await interaction.response.send_message(f"Loaded {extension}", ephemeral=True)


async def setup(client):
    await client.add_cog(reloadExtension(client))