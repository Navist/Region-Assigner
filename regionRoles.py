import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from discord.ext.commands import Bot

count = 0

class regionRoles(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client


    @app_commands.command(name='region', description='Applies the selected region to your Discord nickname.')
    @app_commands.guild_only
    @app_commands.describe(regions='Choose your region from the list.')
    @app_commands.choices(regions=[
        Choice(name='NA: North America', value='NA'),
        Choice(name='AS: Asia', value='AS'),
        Choice(name='AU: Australia', value='AU'),
        Choice(name='EU: Europe', value='EU'),
        Choice(name='JP: Japan', value='JP'),
        Choice(name='KR: Korea', value='KR'),
        Choice(name='NZ: New Zealand', value='NZ'),
        Choice(name='RU: Russia', value='RU'),
        Choice(name='SA: South America', value='SA'),
    ])
    async def region(self, interaction: discord.Interaction, regions: Choice[str]):
        region = regions.value
        new_nick = await self.update_region(f"[{region}] ", interaction.user)
        await self.edit_n_message(interaction, region, new_nick)

    @region.error
    async def region_error(self, interaction, error):
        print(error)
        await interaction.response.send_message(error, ephemeral=True)

    async def edit_n_message(self, interaction, region, new_nick):
        await interaction.user.edit(nick=new_nick)
        await interaction.response.send_message(f"Your region has been updated to {region}", ephemeral=True)


    async def update_region(self, region, user):
        global count
        count += 1

        if user.nick != None:
            if await self.check_bracket(user.nick):
                strip_region = user.nick.split(']')[1]
                strip_spaces = strip_region.strip(' ')
                new_name = region + strip_spaces
            else:
                new_name = region + user.nick
        else:
            new_name = region + str(user)

        return new_name

    async def check_bracket(self, nick):

        if ']' in nick:
            return True
        else:
            return False


async def setup(client):
    await client.add_cog(regionRoles(client))