import numpy as np
from hmmlearn.hmm import GaussianHMM
class HMMFunctions :
    def __init__(self) :
        self.number=1
    def getScoreOfSequence(self,model,frequency,maxLength=20):
        sumProb=0
        sequenceNumber=0
        rest=len(frequency)
        currentPointer=0
        if (rest<maxLength) :
            sumProb+=model.score(frequency[currentPointer:currentPointer+rest])
            sequenceNumber+=1
        else :
            while rest>0 :
                nextSize=min(maxLength,rest)
                rest-=nextSize                
                if (nextSize==maxLength):                    
                    sumProb+=model.score(frequency[currentPointer:currentPointer+nextSize])
                    sequenceNumber+=1
                    currentPointer+=nextSize
        result=sumProb/sequenceNumber
        return sumProb/sequenceNumber

        
