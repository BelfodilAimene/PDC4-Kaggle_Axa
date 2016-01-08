import numpy as np
from ....abstractController.Scorer import Scorer
from ....controller.featureExtractors.SimpleFeatureExtractor import *
from ModelGenerator import ModelGenerator
class HMMBasedScorer(Scorer) :
    def getScores(self,featureMapsList) :
        scoresList=[]
        modelGenerator=ModelGenerator()
        hmmModels=[]
        accelerationSequences=[]
        i=0
        for traceName,featureMap in featureMapsList :
            model=modelGenerator.generateModel("model"+str(i))
            i+=1
            accelerationSequence=[]
            for line in featureMap :
                accelerationSequence.append(line[0,ACCELERATION])
            accelerationSequences.append(accelerationSequence)
            print "size of sequence"
            print len(accelerationSequence)
            print "begin training"
            model.train([accelerationSequence])
            print "end training"
            hmmModels.append(model)
        print "end all training"
        hmmDistancesSum=np.zeros(len(featureMapsList))
        print hmmDistancesSum
        i=0
        for accelerationSequence in accelerationSequences :
            j=0
            print "i :"
            print i
            for model in hmmModels :
                if (i!=j) :
                    prob=model.log_probability(accelerationSequence)
                    print "j :"
                    print j
                    print prob
                    hmmDistancesSum[j]+=prob
                j+=1
            i+=1
        i=0
        print "result :"
        print hmmDistancesSum
        for traceName,featureMap in featureMapsList :    
            scoresList.append((traceName,hmmDistancesSum[i]))
            i+=0
        return np.array(scoresList)
