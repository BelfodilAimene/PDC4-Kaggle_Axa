import numpy as np
import math


class SimpleFeatureExtractor() :
    """
    The sampling rate is supposed to be 1 hz (1 second between each sample)
    """
    
    def getFeatures(self,trace,numberOfQuantile=100) :
        speedFeature=[]
        accelerationFeature=[]
        angularVelocity=[]
        angularAcceleration=[]

        lastEvent=trace[0]

        lastSpeed=0
        lastBearing=0
        lastAngularVelocity=0

        piConstant=math.pi
        
        for currentEvent in trace :
            currentSpeed=currentEvent.distance(lastEvent)

            """
            currentBearing is between 0 and 2*pi
            """
            currentBearing=currentEvent.bearing(lastEvent)

            """
            currentAngularVelocity is between -pi and pi
            """
            currentAngularVelocity=currentBearing-lastBearing
            if (currentAngularVelocity<=-piConstant) : currentAngularVelocity+=2*piConstant
            elif (currentAngularVelocity>piConstant) : currentAngularVelocity-=2*piConstant

            """
            currentAngularAcceleration is between -pi and pi
            """
            currentAngularAcceleration=currentAngularVelocity-lastAngularVelocity
            if (currentAngularAcceleration<=-piConstant) : currentAngularAcceleration+=2*piConstant
            elif (currentAngularAcceleration>piConstant) : currentAngularAcceleration-=2*piConstant
            
            speedFeature.append(currentSpeed)
            accelerationFeature.append(currentSpeed-lastSpeed)
            angularVelocity.append(currentAngularVelocity)
            angularAcceleration.append(currentAngularAcceleration)

            lastSpeed=currentSpeed
            lastBearing=currentBearing
            lastAngularVelocity=currentAngularVelocity
            lastEvent=currentEvent

        sortedSpeedFeature=sorted(speedFeature[2:])
        sortedAccelerationFeature=sorted(accelerationFeature[2:])
        sortedAngularVelocity=sorted(angularVelocity[2:])
        sortedAngularAcceleration=sorted(angularAcceleration[2:])

        sizeOfSortedFeatures=len(sortedSpeedFeature)

        speedCentiles=[]
        accelerationCentiles=[]
        angularVelocityCentiles=[]
        angularAccelerationCentiles=[]

        for i in range(1,numberOfQuantile) :
            ithQuantilIndex=int(sizeOfSortedFeatures*i/numberOfQuantile)
            speedCentiles.append(sortedSpeedFeature[ithQuantilIndex])
            accelerationCentiles.append(sortedAccelerationFeature[ithQuantilIndex])
            angularVelocityCentiles.append(sortedAngularVelocity[ithQuantilIndex])
            angularAccelerationCentiles.append(sortedAngularAcceleration[ithQuantilIndex])

        featuresOfTrace=speedCentiles+accelerationCentiles+angularVelocityCentiles+angularAccelerationCentiles

        return featuresOfTrace
