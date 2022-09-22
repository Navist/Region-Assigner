import discord
from discord.ext import commands
from discord.ext.commands.converter import MemberConverter
import asyncio
import json
import datetime
import time
import random
import os
import consolePrint



class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await consolePrint.console_print("guild-join", f"Invited to {guild.id}:{guild.name}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        pass
        
    @commands.Cog.listener()
    async def on_member_update(self, userA, userB):
        pass

    @commands.Cog.listener()
    async def on_command(self, ctx):
        await  consolePrint.console_print("command", f"{ctx.message.author} issued {ctx.message.content}")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass

async def setup(client):
    await client.add_cog(Events(client))