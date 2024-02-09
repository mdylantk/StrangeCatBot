import random
import requests
import json

#main will load this in form the dialog.jason file
#dialog = json.load(open("dialog.json"))
dialog = {}

def get_greeting():
  responce = random.choice(dialog["greetings"])
  return responce
  
def get_quote():
  request_responce = requests.get("https://api.quotable.io/quotes/random")
  data = json.loads(request_responce.text)
  responce = random.choice(dialog["quoteActions"]).format(
    quote = data[0]["content"],
    author = data[0]["author"]
  )
  return responce

def get_fact():
  request_responce = requests.get("https://catfact.ninja/fact")
  data = json.loads(request_responce.text)
  responce =  "{prefix} ` {fact} ` {suffix}".format(
    prefix = random.choice(dialog["prefix"]),
    fact = data["fact"],
    suffix = random.choice(dialog["suffix"])
  )
  return responce 

def get_joke():
  request_responce = requests.get("https://official-joke-api.appspot.com/random_joke")
  data = json.loads(request_responce.text)
  responce =  "{prefix} {fact} || {punchline} ||".format(
    prefix = random.choice(dialog["prefix"]),
    fact = data["setup"],
    punchline = data["punchline"]
  )
  return responce

def get_error(error_message = "Something broke."):
  responce = random.choice(dialog["errors"]).format(error = error_message)
  return responce

def pick_word(words):
  if "," in words:
    random_words = words.split(",")
    responce = random.choice(dialog["picksActions"]).format(
      option = random.choice(random_words).strip()
    )
    return responce
  else:
    return get_error("The choices need to be seprated by commas `,`.")

def get_cat_picture():
  request_responce = requests.get("https://cataas.com/cat?json=true")
  data = json.loads(request_responce.text)
  responce = "https://cataas.com/cat/"+ data["_id"]
  return responce

#this is for ref sources. may need a better way to keep track of it.
def get_info():
  responce =  "{prefix} {intro}. ||```{data}```|| ".format(
    prefix = random.choice(dialog["prefix"]),
    intro = "I am a random cat bot with random features",
    data = (
      "bot source: https://github.com/mdylantk/StrangeCatBot \n" +
      "api sources: \n" +
      "quote: https://api.quotable.io/quotes/random \n" +
      "fact: https://catfact.ninja/fact \n" +
      "joke: https://official-joke-api.appspot.com/random_joke \n" +
      "picture: https://cataas.com/cat/cute \n"
    )
  )
  return responce

def get_happy():
  responce = random.choice(dialog["happy"])
  return responce