import numpy as np

TIME=0

DISTANCE=1
SPEED=2
ACCELERATION=3
DECELERATION=4

ANGLE=4
ANGULAR_VELOCITY=5
ANGULAR_ACCELERATION=6
ANGULAR_DECELERATION=7

class FeatureExtractor :
    def getFeatureMap(self,trace) :
        timeList=[event.t for event in trace]
        distanceList=self.getDistanceList(trace)

        return np.matrix(zip(timeList,distanceList)) 

    #-----------------------------------------------------------
    def getDistanceList(self,trace) :
        distanceList=[]
        if (trace) :
            d=0
            lastEvent=trace[0]
            for e in trace :
                distanceList.append(d)
                d+=lastEvent.distance(e)
        return distanceList
            
