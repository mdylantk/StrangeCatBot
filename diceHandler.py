

import responses
#todo: handle responces abstractly. also old logic still plug in and
#this is notplug in yet
import numpy
random_state = numpy.random.RandomState()

def roll_dice(dice_string): 
  if "d" not in dice_string:
    return responses.get_error("the format is #d#, where # is a number.")
  split_string = dice_string.split("d")
  split_string[0] = split_string[0].strip()
  split_string[1] = split_string[1].strip()
  if split_string[0].isdigit() and split_string[1].isdigit():
    dice_number = int(split_string[0])
    dice_sides = int(split_string[1])
    if dice_number > 0 and dice_sides > 0:
      roll = random_state.randint(1, dice_sides, dice_number)
      return str(roll) + " for a total of " + str(sum(roll))
    else:
      return responses.get_error("there should not be any negative numbers.")
  else:
    return responses.get_error("there should only be numbers and the d for dice.")