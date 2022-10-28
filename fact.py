from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
import random


class Fact(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def get_fact(self):
        filename = 'facts.txt'
        with open(filename, 'r') as file:
            lines = file.readlines()
            number = random.randint(0, lines.value())
        return lines[number]

            


    @slash_command(name="fact", description="Tell you a random fact.", guild_ids=[959573676892774461])
    async def ping(self, inter: Interaction) -> None:
        filename = 'fact.txt'
        with open(filename, 'r') as file:
            lines = file.readlines()
            number = random.randint(0, lines.value())
        await inter.send(lines[number])




# This goes at the bottom of the file.
def setup(bot: Bot) -> None:
    bot.add_cog(Fact(bot))
