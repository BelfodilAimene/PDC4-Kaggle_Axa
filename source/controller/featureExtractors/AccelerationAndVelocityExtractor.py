from ...abstractController.FeatureExtractor import FeatureExtractor
import numpy as np
import math

FEATURE_NUMBER=6

TIME=0
DISTANCE=1
SPEED=2
ACCELERATION=3
BEARING=4 #in radian
ABSOLUTE_ANGULAR_VELOCITY=5


class AccelerationAndVelocityExtractor(FeatureExtractor) :
    def getFeatureMap(self,trace) :
        if (len(trace)<3) : return []

        result=[]
        lastLine=[0]*FEATURE_NUMBER
        lastEvent=trace[0]
        i=0
        for e in trace :
            newLine=[0]*FEATURE_NUMBER
            timeDifference=e.delai(lastEvent)
            newLine[TIME]=e.t
            newLine[DISTANCE]=e.distance(lastEvent)
            newLine[BEARING]=e.bearing(lastEvent)
            if (timeDifference>0) :
                newLine[SPEED]=newLine[DISTANCE]/timeDifference
                newLine[ACCELERATION]=(newLine[SPEED]-lastLine[SPEED])/timeDifference                
                absoluteAngleDifference=newLine[BEARING]-lastLine[BEARING]                
                newLine[ABSOLUTE_ANGULAR_VELOCITY]=absoluteAngleDifference/timeDifference                
            lastEvent=e
            lastLine=newLine
            result.append(newLine)
        
        #Eliminate element 0 and 1 (false acceleration , ...)
        result=np.matrix(result[2:])
        return result
