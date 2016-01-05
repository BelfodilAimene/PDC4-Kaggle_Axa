import numpy as np
from ....abstractController.Scorer import Scorer
import ModelGenerator
class HMMBasedScorer(Scorer) :
    def getScores(self,featureMapsList) :
        scoresList=[]
        modelGenerator=ModelGenerator()
        hmmModels=[]
        accelerationSequences=[]
        for traceName,featureMap in featureMapsList :
            model=modelGenerator.generate()
            accelerationSequence=[]
            for j in range(len(featureMap)) :
                accelerationSequence.append(featureMap[j][ACCELERATION])
            accelerationSequences.append(accelerationSequence)
            model.train([accelerationSequence])
            hmmModels.append(model)
        hmmDistancesSum=np.zeros(len(featureMapsList))
        i=0
        for accelerationSequence in accelerationSequences :
            j=0
            for model in hmmModels :
                if (i!=j) :
                    hmmDistancesSum[j]+=model.log_probability(accelerationSequence)
                j+=1
            i+=1
        i=0
        for traceName,featureMap in featureMapsList :    
            scoresList.append((traceName,hmmDistancesSum[i]))
            i+=0
        return np.array(scoresList)
