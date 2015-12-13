import numpy as np
import math

TIME=0

DISTANCE=1
SPEED=2
ACCELERATION=3
DECELERATION=4

ANGLE=4 #in radian
ANGULAR_VELOCITY=5
ANGULAR_ACCELERATION=6
ANGULAR_DECELERATION=7

class FeatureExtractor :
    def getFeatureMap(self,trace) :
        if (not trace) : return []

        result=[]
        lastLine=[0,0,0,0,0,0]
        lastEvent=trace[0]

        for e in trace :
            timeDifference=e.delai(lastEvent)
            
            time_feature=e.t
            distance_feature=e.distance(lastEvent)
            speed_feature=distance_feature/timeDifference if (timeDifference>0) else 0
            acceleration_feature=max(speed_feature-lastLine[SPEED],0)/timeDifference if (timeDifference>0) else 0
            deceleration_feature=min(speed_feature-lastLine[SPEED],0)/timeDifference if (timeDifference>0) else 0
            angle_feature=math.atan2(e.y, e.x)
            
            lastLine=[time_feature,distance_feature,speed_feature,acceleration_feature,deceleration_feature,angle_feature]
            lastEvent=e
            
            result.append(lastLine)

        result=np.matrix(result)
        print result
        return result
