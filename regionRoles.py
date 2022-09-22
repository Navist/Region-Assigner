import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from discord.ext.commands import Bot

count = 0

class regionRoles(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    # @app_commands.command(name='na', description='Applies the North America region tag to your nickname.')
    # async def region_NA(self, interaction: discord.Interaction):
    #     region = 'NA'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='sa', description='Applies the South America region tag to your nickname.')
    # async def region_SA(self, interaction: discord.Interaction):
    #     region = 'SA'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='oce', description='Applies the Oceanic region tag to your nickname.')
    # async def region_OCE(self, interaction: discord.Interaction):
    #     region = 'OCE'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='as', description='Applies the Asia region tag to your nickname.')
    # async def region_AS(self, interaction: discord.Interaction):
    #     region = 'AS'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='eu', description='Applies the Europe region tag to your nickname.')
    # async def region_EU(self, interaction: discord.Interaction):
    #     region = 'EU'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='ru', description='Applies the Russia region tag to your nickname.')
    # async def region_RU(self, interaction: discord.Interaction):
    #     region = 'RU'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)

    # @app_commands.command(name='au', description='Applies the Australia region tag to your nickname.')
    # async def region_AU(self, interaction: discord.Interaction):
    #     region = 'AU'
    #     new_nick = await self.update_region(f'[{region}] ', interaction.user)
    #     await self.edit_n_message(interaction, region, new_nick)


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

# async def setup(client: commands.Bot):
#   await client.add_cog(regionRoles(client), guilds=[discord.Object(id=356833056562348042)])

async def setup(client):
    await client.add_cog(regionRoles(client))