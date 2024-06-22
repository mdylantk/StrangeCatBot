import os

import discord
import json
import asyncio

import messageHandler
import debugHandler
import personalityHandler
import responses


###Init Importaint Variables###

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
dir_path = os.path.dirname(os.path.realpath(__file__))

#a shutoff switch. should only be true if bot is running
is_active = False

properties = {}

###Function###
def load_data():
  global properties
  print("loading data from json files")
  properties = load_properties()
  responses.dialog = load_json(dir_path+os.path.sep+'dialog.json')


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

###async functions###
async def update():
  global is_active
  while is_active:
    personalityHandler.update()
    new_activity = personalityHandler.update_activity()
    if new_activity != None:
      await client.change_presence(activity=discord.CustomActivity(
        personalityHandler.activity
      ))
      #print("activity was changed: " + str(new_activity))
    await asyncio.sleep(30)
    
  
###Event Hooks###

@client.event
async def on_ready():
    global is_active
    is_active = True
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.CustomActivity(
      personalityHandler.activity
    ))
    await update()

@client.event
async def on_message(message):
    global properties
    if message.author == client.user:
        return
    results = await messageHandler.handleMessage(message)
    if properties["debug"]["enable"] and properties["debug"]["show_messages"]:
      print(results)
    if results["handled"]:
      personalityHandler.wake(True)
      if "mood" in results:
        personalityHandler.mood += results["mood"]
        personalityHandler.wake(False)
      else:
        personalityHandler.energy -= 1
        personalityHandler.wake(True)
    for signal in results["signals"]:
      if signal == "reload":
        load_data()
    

###Setup### run function and set up states

load_data()

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
