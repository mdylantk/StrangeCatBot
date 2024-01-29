

import responses
#todo: handle responces abstractly. also old logic still plug in and
#this is notplug in yet
import numpy
random_state = numpy.random.RandomState()

def roll_dice(dice_string):
  #this depends on responces. it should handle messages and rolls
  #and responces handle the formating.
  results = {"message":responses.get_error("")}
  if "d" not in dice_string:
    results["message"] = responses.get_error("the format is #d#, where # is a number.")
    return results
  split_string = dice_string.split("d")
  split_string[0] = split_string[0].strip()
  split_string[1] = split_string[1].strip()
  if split_string[0].isdigit() and split_string[1].isdigit():
    dice_number = int(split_string[0])
    dice_sides = int(split_string[1])
    if dice_number > 0 and dice_sides > 0:
      roll = random_state.randint(1, dice_sides, dice_number)
      results = {"rolls":roll,"sum":sum(roll)}
      results["message"] = str(results["rolls"])+" for a total of "+str(results["sum"])
      return results
    else:
      results["message"] = responses.get_error("there should not be any negative numbers.")
  else:
    results["message"] = responses.get_error("there should only be numbers and the d for dice.")
  return results