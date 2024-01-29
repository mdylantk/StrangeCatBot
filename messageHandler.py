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
  message_data = {"command_prefix":"","command":"","message":"","arguments":[]}
  msg = message.content
  #below may be better with a for loop from a list of vaild prefixs
  if (message.content.startswith('meow') or
    message.content.startswith('mew')
  ):
    split_message = message.content.split(" ")
    message_data["command_prefix"] = split_message[0]
    message_data["command"] = split_message[1]
    message_data["message"] = message.content.split(
      message_data["command_prefix"] + " " + message_data["command"]
    )[1]
    message_data["arguments"] = split_message[2:] 
  #arguments will be formated incorrectly when handling any type of string
  #responces after this parse. the commands need to reformat it in such cases

  elif message.content.startswith('$'):
    message_data["command_prefix"] = "$"
    message_data["message"] = message.content.split("$")[1]
    split_message = message_data["message"].split(" ")
    message_data["command"] = message_data["message"].split(" ")[0]
    message_data["message"] = message.content.split(
      message_data["command_prefix"] + message_data["command"] 
    )[1]
    message_data["arguments"] = split_message[1:] 


  #print(message_data)

  if message_data["command"] == "hello":
    await message.channel.send(responses.get_greeting())
  elif message_data["command"] == "quote":
    await message.channel.send(responses.get_quote())
  elif message_data["command"] == "pick":
    await message.channel.send(responses.pick_word(message_data["message"]))
  elif message_data["command"] == "roll":
    await message.channel.send(diceHandler.roll_dice(message_data["message"])["message"])
  elif message_data["command"] == "fact":
    await message.channel.send(responses.get_fact())
  elif message_data["command"] == "joke":
    await message.channel.send(responses.get_joke())