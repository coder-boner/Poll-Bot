#MADE BY Coder-Boner (https://github.com/coder-boner/)
#Repo (https://github.com/coder-boner/Poll-Bot)

import discord
from discord.ext import commands

# Replace TOKEN with your bot's token
BOT_TOKEN = 'TOKEN'
# Replace CHANNEL_ID with your desired channel id
suggestion_channel_id = CHANNEL_ID

# Intents (required to access certain features)
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# The event for creating the thread and reacting to message
@bot.event
async def on_message(message):
    # Makes sure the bot does not react ot its own message
    if message.author == bot.user:
        return

    # Compares the channel id that the message was sent in
    # and if it is not it will not continue
    if message.channel.id == suggestion_channel_id:

        print(f'Suggestion from {message.author}: {message.content}')

        # Reacting to said message
        try:
            await message.add_reaction('✔')
            await message.add_reaction('❌')
            await message.create_thread(name=f'{message.author.name} Thread.', slowmode_delay=15)

        # To catch errors/exceptions when they occur
        except discord.HTTPException as e:  # Catch Discord-specific exceptions
            print(f"Error reacting to the message: {e}")
        except Exception as e:  # Catch any other general exceptions
            print(f"Unexpected error: {e}")


# Run the bot
bot.run(BOT_TOKEN)
