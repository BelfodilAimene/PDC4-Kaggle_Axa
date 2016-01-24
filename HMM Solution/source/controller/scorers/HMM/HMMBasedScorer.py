import numpy as np
from ....abstractController.Scorer import Scorer
from ....controller.featureExtractors.AccelerationAndVelocityExtractor import *
from ..utils.Utils import *
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt
from HMMFunctions import HMMFunctions
class HMMBasedScorer(Scorer) :
    
    def getScores(self,featureMapsList) :
        scoresList=[]
        accelerationFrequencies1ForLearn=[]
        accelerationFrequencies2ForLearn=[]
        accelerationFrequencies3ForLearn=[]
        accelerationFrequencies1=[]
        accelerationFrequencies2=[]
        accelerationFrequencies3=[]
        velocityFrequencies1ForLearn=[]
        velocityFrequencies2ForLearn=[]
        velocityFrequencies3ForLearn=[]
        velocityFrequencies1=[]
        velocityFrequencies2=[]
        velocityFrequencies3=[]
        hmmFunctions=HMMFunctions()
        for traceName,featureMap in featureMapsList :        
            accelerationSequence=[row[0,ACCELERATION] for row in featureMap]
            frequencies1=getMaximalFrequencies(accelerationSequence,slidingWindowSize=40, stepSize=20,numberOfFrequency=3)
            accelerationFrequencies1ForLearn+=[row[0] for row in frequencies1]
            accelerationFrequencies2ForLearn+=[row[1] for row in frequencies1]
            accelerationFrequencies3ForLearn+=[row[2] for row in frequencies1]
            accelerationFrequencies1.append([row[0] for row in frequencies1])
            accelerationFrequencies2.append([row[1] for row in frequencies1])
            accelerationFrequencies3.append([row[2] for row in frequencies1])


            velocitySequence=[row[0,ABSOLUTE_ANGULAR_VELOCITY] for row in featureMap]
            frequencies2=getMaximalFrequencies(velocitySequence,slidingWindowSize=40, stepSize=20,numberOfFrequency=3)
            velocityFrequencies1ForLearn+=[row[0] for row in frequencies2]
            velocityFrequencies2ForLearn+=[row[1] for row in frequencies2]
            velocityFrequencies3ForLearn+=[row[2] for row in frequencies2]
            velocityFrequencies1.append([row[0] for row in frequencies2])
            velocityFrequencies2.append([row[1] for row in frequencies2])
            velocityFrequencies3.append([row[2] for row in frequencies2])

        TrainedList=np.column_stack([accelerationFrequencies1ForLearn,accelerationFrequencies2ForLearn,accelerationFrequencies3ForLearn,velocityFrequencies1ForLearn,velocityFrequencies2ForLearn,velocityFrequencies3ForLearn])
        model = GaussianHMM(n_components=6, covariance_type="diag", n_iter=1000).fit(TrainedList)
        hmmScores=[]
        for i in range(len(accelerationFrequencies1)) :                        
            traceFrequency=np.column_stack([accelerationFrequencies1[i],accelerationFrequencies2[i],accelerationFrequencies3[i],velocityFrequencies1[i],velocityFrequencies2[i],velocityFrequencies3[i]])
            hmmScores.append(hmmFunctions.getScoreOfSequence(model,traceFrequency))
        i=0
        for traceName,featureMap in featureMapsList :    
            scoresList.append((traceName,hmmScores[i]))
            i+=1
        return np.array(scoresList)
    
    
