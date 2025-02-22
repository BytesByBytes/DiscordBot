import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX', '!')

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)

# Define bot intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Load cogs from the "cogs" folder
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logging.info('------')
    # Optionally, you can load additional cogs here if not auto-loaded.
    # For example, load a cog from events:
    # bot.load_extension("events.on_ready")

def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            extension = f"cogs.{filename[:-3]}"
            try:
                bot.load_extension(extension)
                logging.info(f"Loaded extension '{extension}'")
            except Exception as e:
                logging.error(f"Failed to load extension {extension}.", exc_info=e)

if __name__ == '__main__':
    load_extensions()
    bot.run(TOKEN)
