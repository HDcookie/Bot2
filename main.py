from nextcord.ext.commands import Bot
import nextcord

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = Bot(command_prefix="$", description="hi", intents=intents)

def get_bot_token():
    filename = 'token.txt'
    with open(filename, 'r') as file:
        return file.read()


bot.load_extension("ping")
bot.load_extension("count")
bot.load_extension("fact")



print("Starting bot...")
bot.run(get_bot_token())
print("disabling bot.")
