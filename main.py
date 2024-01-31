
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

dir_path = os.path.dirname(os.path.realpath(__file__))

def load_json(path):
  data = {}
  with open(path) as file :
    data = json.load(file)
    file.close()
  return data

properties = [load_json(dir_path+os.path.sep+'defaultProperties.json'),{}]
if os.path.isfile(dir_path+os.path.sep+'properties.json'):
  properties_changes = load_json(dir_path+os.path.sep+'properties.json')
  properties[1] = properties_changes
  

def get_property(property_group, property_name):
  if property_group in properties[1]:
    if property_name in properties[1][property_group]:
      return properties[1][property_group][property_name]
  return properties[0][property_group][property_name]

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
  token = os.getenv("TOKEN") or get_property("discord", "key")
  if token == "":
    raise Exception("Please add your token to the Secrets pane or properties file.")
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
