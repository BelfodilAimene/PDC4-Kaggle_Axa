from ...abstractController.FeatureExtractor import FeatureExtractor
import numpy as np
import math

FEATURE_NUMBER=9

TIME=0
DISTANCE=1
SPEED=2
ACCELERATION=3
DECELERATION=4
BEARING=5 #in radian
ABSOLUTE_ANGULAR_VELOCITY=6
ANGULAR_ACCELERATION=7
ANGULAR_DECELERATION=8

#Each feature is divided by its scale to normalise it !
knownScale=[1,1,50,20,20,2*math.pi,math.pi,math.pi,math.pi]


class SimpleFeatureExtractor(FeatureExtractor) :
    def getFeatureMap(self,trace) :
        if (len(trace)<3) : return []

        result=[]
        lastLine=[0]*FEATURE_NUMBER
        lastEvent=trace[0]

        for e in trace :
            newLine=[0]*FEATURE_NUMBER

            timeDifference=e.delai(lastEvent)
            
            newLine[TIME]=e.t
            newLine[DISTANCE]=e.distance(lastEvent)
            newLine[BEARING]=e.bearing(lastEvent)

            if (timeDifference>0) :
                newLine[SPEED]=newLine[DISTANCE]/timeDifference
                newLine[ACCELERATION]=max(newLine[SPEED]-lastLine[SPEED],0)/timeDifference
                newLine[DECELERATION]=max(lastLine[SPEED]-newLine[SPEED],0)/timeDifference

                absoluteAngleDifference=abs(newLine[BEARING]-lastLine[BEARING])
                if (absoluteAngleDifference>math.pi) : absoluteAngleDifference=2*math.pi-absoluteAngleDifference 
                newLine[ABSOLUTE_ANGULAR_VELOCITY]=absoluteAngleDifference/timeDifference
                newLine[ANGULAR_ACCELERATION]=max(newLine[ABSOLUTE_ANGULAR_VELOCITY]-lastLine[ABSOLUTE_ANGULAR_VELOCITY],0)/timeDifference
                newLine[ANGULAR_DECELERATION]=max(lastLine[ABSOLUTE_ANGULAR_VELOCITY]-newLine[ABSOLUTE_ANGULAR_VELOCITY],0)/timeDifference
            
            result.append(newLine)

            lastEvent=e
            lastLine=newLine

        #Eliminate line 0 and 1 (false acceleration , ...)
        result=np.matrix(result[2:])
        return result
