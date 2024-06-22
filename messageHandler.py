#this will handle the message processing
import responses
import diceHandler

async def handleMessage(message):
  #if message.author == client.user:
  #  return
  #message data is a place holder for parced message
  #message will change at diffrence state of the parcing. 
  #argument is an optional parcing of parameter in the message
  #which is usally done last if used.
  #command_prefix is being stored incase the triggeing word would reflect bot responce
  message_data = {
    "command_prefix":"",
    "command":"",
    "message":"",
    "arguments":[],
    "handled":False,
    "signals":[]
  }
  #handle the message in lowercase for now. 
  msg = message.content.lower()
  #below may be better with a for loop from a list of vaild prefixs
  if (msg.startswith('meow') or
    msg.startswith('mew')
  ):
    split_message = msg.split(" ")
    message_data["command_prefix"] = split_message[0]
    if len(split_message) > 1:
      message_data["command"] = split_message[1]
      message_data["message"] = msg.split(
        message_data["command_prefix"] + " " + message_data["command"]
      )[1]
      message_data["arguments"] = split_message[2:] 
  #arguments will be formated incorrectly when handling any type of string
  #responces after this parse. the commands need to reformat it in such cases
  elif msg.startswith('$'):
    message_data["command_prefix"] = "$"
    message_data["message"] = msg.split("$")[1]
    split_message = message_data["message"].split(" ")
    message_data["command"] = message_data["message"].split(" ")[0]
    message_data["message"] = msg.split(
      message_data["command_prefix"] + message_data["command"] 
    )[1]
    message_data["arguments"] = split_message[1:] 

  
  if message_data["command_prefix"] == "":
    #currently not analying messages here, so this end the logic
    #so the rest if the logic wont run and do odd things
    return message_data
  elif message_data["command_prefix"] == "meows":
    await message.channel.send(responses.get_greeting())
    message_data["handled"] = True
    return message_data
  else:
    responce = handleCommands(message_data)
    if responce is not None:
      await message.channel.send(responce)
      message_data["handled"] = True
      return message_data
    else:
      return message_data

def handleCommands(message_data):
  return_value = None
  if (message_data["command"] == "hello" or 
    message_data["command"] == "hi" or
    message_data["command"] == "hey" or
    message_data["command"] == "meows"
   ):
    return_value = responses.get_greeting()
  elif message_data["command"] == "quote":
    return_value =responses.get_quote()
  elif message_data["command"] == "pick":
    return_value = responses.pick_word(message_data["message"])
  elif message_data["command"] == "roll":
    return_value = (
      diceHandler.roll_dice(message_data["message"])["message"]
    )
  elif message_data["command"] == "fact":
    return_value =responses.get_fact()
  elif message_data["command"] == "joke":
    return_value =responses.get_joke()
  elif (message_data["command"] == "picture" or
        message_data["command"] == "pic" or
        message_data["command"] == "photo" or
        message_data["command"] == "photograph"
      ):
    return_value = responses.get_cat_picture()
  elif message_data["command"] == "info":
    return_value = responses.get_info()

  elif message_data["command"] in [
    "pets","*pets*","pet","*pet*",
    "nuzzles","*nuzzles*",
    "snuggles","*snuggles*",
    "love", "loves",
  ]:
    message_data["mood"] = 1
    return_value = responses.get_happy()
  elif message_data["command"] == "reload":
    return_value = "Meow will try to rethink things"
    message_data["signals"].append("reload")
  
  message_data["response"] = return_value
  return return_value