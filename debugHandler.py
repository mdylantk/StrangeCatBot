#this is reserve for handling debug messages
#or anything relating to debugging the bot

properties = {
  "enable":False,
  "show_messages":False
}

def print_error(source = "undefined", error = "error", data = ""):
  if properties["enable"] is True:
    print(f"[{source}] {error}:{data}")

def print_message(source = "undefined", message = "message"):
  if properties["show_messages"] is True:
    print(f"[{source}] {message}")