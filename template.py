#DO NOT USE THIS FILE, COPY IT TO YOUR PROJECT AND EDIT IT
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog


class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="template", description="A template command, not ment to be used.", guild_ids=[959573676892774461])#might need to change
    async def ping(self, inter: Interaction) -> None:
        await inter.send("pong")




# This goes at the bottom of the file.
def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))
