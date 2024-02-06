#this will hold the state of the bot personality and/or mood
#or at least handle all files related to personality and memory

#mood will be a range of -1 to 1 or -100 to 100
#base on if int or float will suit it better
mood = 0
energy = 100 #0-100
#how long the cat is napping. use as a way to know when
#the cat slept enough since energy should regenate when sleeping
sleeping_time = 0

#currectly selected activity. may be change to a ref or path
activity = "*being a lazy cat*"

###note and stuff###
#first goal is simple. A mood changer base on time and random choices
#energy may increase or decrease over time. actions may also decrease it
#energy reflect the sleepy state(naping) and active state(hyper or playfullness)
#may need to import discord.py to allow this to update the status when there is a change

#also need group sorted array of activites. this could be a nested array
#or a dictionary of type(like sleepy, active, default)
#if nested array, the numbers of the first entry will be related to energy level
#with a random roll to see which array to choise if the index is not a whole number