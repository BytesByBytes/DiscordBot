import os
import discord
from discord.ext import commands
import logging
import config
import discord_token


# Retrieve configuration from config.py
TOKEN = discord_token.DISCORD_TOKEN
PREFIX = discord_token.BOT_PREFIX

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define bot intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logging.info('------')

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
