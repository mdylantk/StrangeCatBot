import random
import requests
import json

greetings = ["Meow!", "Hellow", "Mew hi!", "Meow mew", "*lays on side* Meow","*purrs*"]
quote_action = [
  "*knocks a book off a shelf." +
    " The book opens to a page with the following quote:* ` {0} -{1}`",
  "*Lays on an open book exposing the quote:* ` {0} -{1}`"
]
errors = ["Meow is confused. {}", "Mew is confused. {}", "*Rolls around.* {}"]
picks_actions = ["*paws* `{}`", "Mew what about `{}`", "Meow picks `{}`",
                 "*nibbles `{}`*"]


def get_greeting():
  return random.choice(greetings)
  
def get_quote():
  request_responce = requests.get("https://api.quotable.io/quotes/random")
  data = json.loads(request_responce.text)
  return random.choice(quote_action).format(data[0]["content"],data[0]["author"])

def get_fact():
  request_responce = requests.get("https://catfact.ninja/fact")
  data = json.loads(request_responce.text)
  return "meow `" + data["fact"] + "`"

def get_joke():
  request_responce = requests.get("https://official-joke-api.appspot.com/random_joke")
  data = json.loads(request_responce.text)
  return "meow " + data["setup"] + " || " + data["punchline"] + "||"

def get_error(error_message = "Something broke."):
  return random.choice(errors).format(error_message)

def pick_word(words):
  if "," in words:
    random_words = words.split(",")
    return random.choice(picks_actions).format(random.choice(random_words).strip())
  else:
    return get_error("The choices need to be seprated by commas `,`.")