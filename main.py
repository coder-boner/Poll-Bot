import os
import random
import time
import asyncio
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import app_commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from itertools import cycle
import json
import random

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.reactions = True
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'TOKEN'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Bot is ready')



bot.run(TOKEN)