from ...abstractController.Normalizer import Normalizer
import time

class MinMaxNormalizer(Normalizer) :
    def normalize(self,featureMapsList) :
        staringTime=time.time()
        if (not featureMapsList) : return featureMapsList

        featureNumber=featureMapsList[0][1].shape[1]-1
        minPerFeature=[float("inf")]*featureNumber
        maxPerFeature=[-float("inf")]*featureNumber

        for traceName,featureMap in featureMapsList :
            for j in range(featureNumber) :
                #The column 0 is always the time (not normalized)
                featureColumn=featureMap[:,j+1]
                minPerFeature[j]=min(min(featureColumn)[0,0],minPerFeature[j])
                maxPerFeature[j]=max(max(featureColumn)[0,0],maxPerFeature[j])

        elapsed_time=(time.time()-staringTime)
        print "-"*40
        print "min and max Calcul time : {0}s".format(elapsed_time)
        print "-"*40
        print minPerFeature
        print "-"*40
        
        for traceName,featureMap in featureMapsList :
            for j in range(featureNumber) :
                quotient=maxPerFeature[j]-minPerFeature[j]
                featureMap[:,j+1]=(featureMap[:,j+1]-minPerFeature[j])/quotient if quotient>0 else 0

        elapsed_time=(time.time()-staringTime)
        print "-"*40
        print "Normalisation time : {0}s".format(elapsed_time)
        print "-"*40
        return featureMapsList
