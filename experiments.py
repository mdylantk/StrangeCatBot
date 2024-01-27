import numpy

def reset_random_state(seed = 0):
  return numpy.random.RandomState(seed)

def random_map(x, y, random_state):
  #placeholder to generate a 2d map of random numbers. currently
  #a range or 0-1 as a float.
  return random_state.rand(x,y)