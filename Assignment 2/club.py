""" Club Class for CP1200 Assignment 2 - 2014-Block 7 
    Douglas Callaway
    21/07/2014 

Pseudocode:

class Club
    constructor(name, distance)
        instance.clubName(name)
        instance.averageHitDistance(averageHitDistance)
        instance.swingStrength(100)
        instance.shotDistance(0)
    
    basic getters for clubInfo, shotDistance
    
    method setSwingStrength(lower,upper)
    (used to calculate the shot distance given lower and upper % strengths) 
        instance.swingStrength = (random integer between lower and upper) / 100
    
    method swing(strength)
        instance.shotDistance = instance.averageHitDistance x instance.swingStrength (integer)
    
    method shortPut(strength, distanceToHole, minPut)
        instance.shotDistance = maximum of minPut and (distanceToHole x instance.swingStrength) (integer) 
"""

'''Club class - stores a club's average hit distance, 
calculates and stores a shot distance
'''
from random import randint
class Club:
          
    def __init__(self, name, distance):
        """ Initialize a Club instance.
        name -- name of the club
        distance -- average meters the club hits (integer; default = 0)
        """
        self._clubName = name
        self._averageHitDistance = distance
        self._swingStrength = 100 
        self._shotDistance = 0  
        
    def getClubInfo(self):
        """Return the club name and its average hit distance"""
        return self._clubName + " (" + str(self._averageHitDistance) + ")"
    
    def getShot(self):
        """Return the distance (meters) of the last shot as an integer"""
        return self._shotDistance
    
    def setSwingStrength(self, lower, upper):
        """Set the swing strength for the next shot between the lower and upper % limits."""
        self._swingStrength = randint(lower, upper) / 100
    
    def swing(self):
        """Set the shot distance for a full swing from the current strength."""
        self._shotDistance = int(self._averageHitDistance * self._swingStrength)
    
    def shortPut(self, distanceToHole, minPut):
        """Calculate the shot distance of a short put.
        --max function ensures at least the minimum put is achieved
        """
        self._shotDistance = int(max(minPut, distanceToHole * self._swingStrength))
