#StudyCheckLib
class Spot:
    #Constructor
    def __init__(self,size,noise,availability,permissions=0,usage=0): # Need to set Default Values
        self.size=size #How many seats/people can use it?
        self.noise=noise #How loud/quiet is it?
        self.availability=availability #Is it open year round, just during exams, and what are the hours
        self.permissions=permissions #Do you need to talk to someone first before using?
        self.usage=usage # Is the room being used now?

    #Mutators -- Self explanatory mostly, these functions set/update class parameters
    def setSize(self,s):
        self.size = s
    def setNoise(self,n):
        self.noise=n
    def setAvailability(self,a):
        self.availability = a
    def setPermissions(self,p):
        self.permissions = p
    def setUsage(self,u):
        self.usage = u

    #Accessors -- Again Pretty easy to understand, these functions access parameters
    def getSize(self):
        return self.size
    def getNoise(self):
        return self.noise
    def getAvailability(self):
        return self.availability
    def getPermissions(self):
        return self.availability
    def getUsage(self):
        return self.usage
        
class Floor:
    #Constructor
    def __init__(self,spots):
        self.spots = spots
        
    #Mutators
    def addSpot(self,s):
        self.spots.append(s)
    def removeSpot(self,spotIndex):
        self.spots.pop(spotIndex)
        
    #Accessors
    def getAllSpots(self):
        return self.spots
    def getFreeSpots(self):
        F=[]
        for i in spots:
            if i.getUsage() == 0: #if the usage of a spot is 0, add it to the list of Free Spots
                F.append(i)
        return F

# To be added to    
class Building:
    def __init__(self,
class Campus:

    def __init__(self,):
        
