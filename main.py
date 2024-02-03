import os

import discord
import json

import messageHandler
import debugHandler
import personalityHandler
import responses


###Init Importaint Variables###

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dir_path = os.path.dirname(os.path.realpath(__file__))

properties = {}

###Function###

def load_json(path):
  data = {}
  with open(path) as file :
    data = json.load(file)
    file.close()
  return data
  
#making this logic a function incase a hot reload of this is needed at any point
def load_properties():
  properties = load_json(dir_path+os.path.sep+'defaultProperties.json')
  if os.path.isfile(dir_path+os.path.sep+'properties.json'):
    properties_changes = load_json(dir_path+os.path.sep+'properties.json')
    for property_group in properties_changes:
      if property_group in properties:
        for property_name in properties_changes[property_group]:
          properties[property_group][property_name] = (
            properties_changes[property_group][property_name]
          )
      else:
        properties[property_group] = properties_changes[property_group]
  #update the properties of other files that depends on it
  if "debug" in properties:
    debugHandler.properties = properties["debug"]
  return properties
  

def get_property(property_group, property_name):
  #comment out section is incase a check is needed. 
  #currently this function is now redundent
  #if property_group in properties:
  #  if property_name in properties[property_group]:
  #    return properties[property_group][property_name]
  #  else:
  #    return None
  #else:
  #  return None
  return properties[property_group][property_name]

###Event Hooks###

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.CustomActivity(
      personalityHandler.activity
    ))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await messageHandler.handleMessage(message)

###Setup### run function and set up states

properties = load_properties()

responses.dialog = load_json(dir_path+os.path.sep+'dialog.json')

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
