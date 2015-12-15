from ...abstractController.Normalizer import Normalizer

class MinMaxNormalizer(Normalizer) :
    def normalize(self,featureMapsList) :
        if (not featureMapsList) :
            return featureMapsList

        featureNumber=featureMapsList[0][1].shape[1]-1
        minPerFeature=[float("inf")]*featureNumber
        maxPerFeature=[-float("inf")]*featureNumber

        for traceName,featureMap in featureMapsList :
            for j in range(featureNumber) :
                #The column 0 is always the time (not normalized)
                featureColumn=featureMap[:,j+1]
                minPerFeature[j]=min(min(featureColumn).item(0,0),minPerFeature[j])
                maxPerFeature[j]=max(max(featureColumn).item(0,0),maxPerFeature[j])

        for traceName,featureMap in featureMapsList :
            for j in range(featureNumber) :
                quotient=maxPerFeature[j]-minPerFeature[j]
                featureMap[:,j+1]=(featureMap[:,j+1]-minPerFeature[j])/quotient if quotient>0 else 0
                
        print "-"*40
            
        return featureMapsList
