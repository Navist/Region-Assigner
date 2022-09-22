import discord
import json
import asyncio
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import traceback


#https://discord.com/oauth2/authorize?client_id=1012726552003358862&permissions=0&scope=bot%20applications.commands


BOT_PREFIX = '>'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.integrations = True

client = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True, intents=intents)
client.secrets = {}
EXTENSIONS = ['regionRoles', 'reloadExtension', 'commands'] # 'purge' 'proViewer'  

with open('secrets.json', 'r') as f:
    client.secrets = json.load(f)

DiscordToken = client.secrets['discordToken']

async def main():
    print('-- RegionBot Initialization --')
    print(datetime.now())    

    async with client:
        for extension in EXTENSIONS:
            try:
                await client.load_extension(extension)
                print(f'[MODULE-LOAD] | {extension}')
            except Exception as error:
                print(traceback.print_exc())
                print(f'[MODULE-ERROR] | {extension} could not be loaded. \n{error}')

        await client.start(DiscordToken)

asyncio.run(main())

# client.run(DiscordToken)