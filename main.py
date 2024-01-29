
# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

#this will set up the bot, most fubctionality should be hosted in diffrent files
import discord

import messageHandler
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

properties = json.load(open('properties.json'))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.CustomActivity('*being a lazy cat*'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await messageHandler.handleMessage(message)


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    if properties["defaults"]["key"] != "":
      token = properties["defaults"]["key"]
    else:
      raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
