
""" interestPoints.py: Find a list of interest points given some constraints """

__author__      = "Pedro Herruzo"
__copyright__   = "Copyright 2016 Pedro Herruzo"

import pandas as pd
import numpy as np
import datetime

'''
  PROBLEM: Let sagrada_familia, pedrera, parc_guell... be a points of interest defined by a prize, average_visit_time, location and time (opening times).
	   Let Joan be an user defined by amount (amount of money he want to spend), places_to_visit (amount of places he want to visit) and time (the time he can visit the places).
	   
	   As You can guess, the goal is offer to Joan a list(s) with the number of places he wants to visit that fits with his time and amount.
  
  ASSUMPTIONS: 1. We assume for simplicity, that our places are located in a straight.
  
  TODO: Decrease user Time by the time that requeries the travel from one point of interest to another.
'''


def timeFits(timeA, timeB, intersectionTime):
  """ Check if both times have an intersection greater or equal to intersectionTime.
  
      Parameters:
	timeA: must be a list with only one dict containing keys 'start' and 'end' with values of type datetime.time(hour, minuts) 
	timeB: must be a list of dicts containing keys 'start' and 'end' with values of type datetime.time(hour, minuts)
	intersectionTime: must be a type type datetime.time(hour, minuts)
      
      Example: timeA = [{'start':time(10), 'finish':time(14)}]
	       timeB = [{'start':time(10), 'finish':time(14)}, {'start':time(16),'finish':time(19)}]
	       intersectionTime = time(2)
	       
      Return: None, if times haven't an intersection greater or equal to intersectionTime
	      start time of the intersection, otherwise.
  """
  fit = None
  finalStartIntersection = time(23)
  
  
  for times in timeB:
    #print times, '\n', timeA[0], '\n', '\n'
    startIntersection = max(timeA[0]['start'], times['start'])
    finishIntersection = min(timeA[0]['finish'], times['finish'])
    
    # Check if the intersection is enought for the constraint intersectionTime
    if finishIntersection-startIntersection >= intersectionTime:
      # Check if the new intersection is earlier than the previous one
      if startIntersection < finalStartIntersection:
	finalStartIntersection = startIntersection

  if finalStartIntersection != time(23):
    fit = finalStartIntersection
  
  return fit
  

def fits(user, placeDefinition):
  return placeDefinition['prize'] <= user['amount'] and timeFits(user['time'], placeDefinition['time'], placeDefinition['average_visit_time']) 

def time(hour, minuts=0):
  #return datetime.time(hour, minuts)
  return datetime.datetime(1,1,1,hour,minuts)

def timeLapse(hours, minuts=0):
  return datetime.timedelta(0, hours*60*60+minuts*60)

# Let's define some points of interest
sagrada_familia = {'prize':10, 'average_visit_time':timeLapse(2), 'location':9, 'time':[{'start':time(10), 'finish':time(14)}, {'start':time(16),'finish':time(19)}]}

pedrera = {'prize':5, 'average_visit_time':timeLapse(2), 'location':3, 'time':[{'start':time(10), 'finish':time(14)}, {'start':time(15),'finish':time(19)}]}

parc_guell = {'prize':3, 'average_visit_time':timeLapse(3), 'location':5, 'time':[{'start':time(7), 'finish':time(22)}]}

museo_picaso = {'prize':12, 'average_visit_time':timeLapse(3), 'location':20, 'time':[{'start':time(10), 'finish':time(14)}, {'start':time(15),'finish':time(19)}]}

museo_ciencia = {'prize':9, 'average_visit_time':timeLapse(3), 'location':1, 'time':[{'start':time(10), 'finish':time(14)}, {'start':time(15),'finish':time(20)}]}

forum = {'prize':4, 'average_visit_time':timeLapse(4), 'location':25, 'time':[{'start':time(10), 'finish':time(17)}]}

# Let's add all of them to a dict
interestPoints = {'sagrada_familia':sagrada_familia, 'pedrera':pedrera, 'parc_guell':parc_guell, 'museo_picaso':museo_picaso, 'museo_ciencia':museo_ciencia, 'forum':forum}

# Let's define a user
Joan = {'amount':30, 'places_to_visit':3, 'time':[{'start':time(13), 'finish':time(20)}]}

# Our problem has well defined constraints, so lets generate a list with all places that fits with Joan
fitList = [(interestPoint,fits(Joan, placeDefinition)) for interestPoint,placeDefinition in interestPoints.items() if fits(Joan, placeDefinition)]
#fitList = [(interestPoint) for interestPoint,placeDefinition in interestPoints.items() if fits(Joan, placeDefinition)]

print fitList



'''
# Test timeFits(timeA, timeB, intersectionTime) function
a = [{'start':time(13), 'finish':time(20)}]
b = [{'start':time(10), 'finish':time(14)}, {'start':time(17),'finish':time(20)}]

#a = [{'start':time(13), 'finish':time(18)}]
#b = [{'start':time(10), 'finish':time(14)}, {'start':time(16),'finish':time(19)}]
c = timeLapse(3)

print a,'\n' 
print b,'\n' 
print c,'\n' 

print 'output: ', timeFits(a,b,c)
'''

