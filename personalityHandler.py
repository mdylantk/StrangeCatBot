#this will hold the state of the bot personality and/or mood
#or at least handle all files related to personality and memory

from math import remainder
import random

#print(random.randrange(1,10))

#mood will be a range of -1 to 1 or -100 to 100
#base on if int or float will suit it better
mood = random.randrange(0,100) + 1
energy = random.randrange(0,100) + 1
#how long the cat is napping. use as a way to know when
#the cat slept enough since energy should regenate when sleeping
sleeping_time = 0

#currectly selected activity. may be change to a ref or path
state = []
activity = "*being a lazy cat*"
#activity_list is a placeholder
activity_list = {
  "sleep":"*is sleeping*",
  "nap":"*is taking a nap*",
  "default":"*being a lazy cat*",
  "sleepy":"*looks tired*",
  "hyper":"*is running all over the place*",
  "moody":"*looks grumpy*",
  "happy":"*snuggling in a ball and purring*"
}

def wake(forced = False):
  global state; global energy; global sleeping_time; global mood;
  sleeping_time = 0
  if energy < 1:
    energy += random.randrange(0,10) + 1
  if forced == True and "sleep" in state:
    mood -= random.randrange(0,10) + 1
  if "sleep" in state:
      state.remove("sleep")
  if "nap" in state:
      state.remove("nap")

def update_activity():
  global state; global energy; global sleeping_time; global mood; global activity;
  return_value = activity_list["default"]
  if "sleep" in state:
    return_value = activity_list["sleep"]
  elif "nap" in state:
    return_value = activity_list["nap"]
  elif energy < 10:
    return_value = activity_list["sleepy"]
  elif energy > 60:
    return_value = activity_list["hyper"]
  elif mood < -50:
    return_value = activity_list["moody"]
  elif mood > 50:
    return_value = activity_list["happy"]
  if activity != return_value:
    activity = return_value
  else:
    return_value = None
  return return_value

#todo: add a timer and add an activity updater. Also test below
def update(mood_mod=1,energy_mod=1,sleeping_time_mod=1):
  global mood; global energy; global sleeping_time; global state
  if "sleep" in state or "nap" in state:
    energy += energy_mod * 1
    mood += mood_mod * random.randrange(0,2)
    sleeping_time += sleeping_time_mod * 1
  else:
    energy += energy_mod * random.randrange(-1,1)
    mood += mood_mod * random.randrange(-1,2)

  if energy <= 0:
    if energy < 0:
      energy = 0
    if "sleep" not in state or "nap" not in state:
      random_roll = random.randrange(0,100) + 1
      if random_roll >= 75:
        state.append("sleep")
      else:
        state.append("nap")
  elif energy > 100:
    energy = 100

  if mood < -100:
    mood = -100
  elif mood > 100:
    mood = 100

  if sleeping_time > 100:
    wake()
    #sleeping_time = 0
    #if "sleep" in state:
    #  state.remove("sleep")
    #if "nap" in state:
    #  state.remove("nap")
  elif sleeping_time > 20 and "nap" in state:
    if random.randrange(0,100) + 1 <= sleeping_time:
      state.remove("nap")

  return False
  #print("mood: " + str(mood))
  #print("energy: " + str(energy))
  #print("sleep: " + str(sleeping_time))
  #print(state)
  
###note and stuff###
#first goal is simple. A mood changer base on time and random choices
#energy may increase or decrease over time. actions may also decrease it
#energy reflect the sleepy state(naping) and active state(hyper or playfullness)
#may need to import discord.py to allow this to update the status when there is a change

#also need group sorted array of activites. this could be a nested array
#or a dictionary of type(like sleepy, active, default)
#if nested array, the numbers of the first entry will be related to energy level
#with a random roll to see which array to choise if the index is not a whole number