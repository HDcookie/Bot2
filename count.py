from pydoc import cli
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class Count(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        self.message = message.content
        print(f"message recieved: {self.message}")




# This goes at the bottom of the file.
def setup(bot: Bot) -> None:
    bot.add_cog(Count(bot))
