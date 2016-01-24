import numpy as np
from sklearn.ensemble import RandomForestClassifier

class DriverModelScorer :
    def __init__(self,oneDriverFeatures,listOfFalseTracesFeatures,crossValidationFoldSize=10) :
        self.oneDriverFeatures=oneDriverFeatures
        self.listOfFalseTracesFeatures=listOfFalseTracesFeatures

        self.crossValidationFoldNumber=len(self.oneDriverFeatures)/crossValidationFoldSize
        self.sizeOfTestList=crossValidationFoldSize
        self.sizeOfTrainList=len(self.oneDriverFeatures)-self.sizeOfTestList

        self.TruePositive=0
        self.TrueNegative=0
        self.FalsePositive=0
        self.FalseNegative=0

    def getScores(self) :    
        scoresList=[]
        falseFeaturesForTrain=self.listOfFalseTracesFeatures[:self.sizeOfTrainList]
        falseFeaturesForTest=self.listOfFalseTracesFeatures[self.sizeOfTrainList:]

        for i in range(self.crossValidationFoldNumber) :
            trueFeaturesForTrain=self.getTrueFeaturesForTrain(i)
            trueFeaturesForTest=self.extractFeatures(i*self.sizeOfTestList,(i+1)*self.sizeOfTestList)
            scoresList+=self.getScoresForTrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest)
        
        return scoresList
    
    def getTrueFeaturesForTrain(self,currentIteration) :
        beginIndex=currentIteration*self.sizeOfTestList
        trueFeaturesForTrain=self.extractFeatures(0,beginIndex)
        trueFeaturesForTrain+=self.extractFeatures(beginIndex+self.sizeOfTestList,len(self.oneDriverFeatures))
        return trueFeaturesForTrain

    def extractFeatures(self,minValue,maxValue) :
        sublistOfFeatures=[]
        for i in range(minValue,maxValue) :
            traceName,featuresList=self.oneDriverFeatures[i]
            sublistOfFeatures.append(featuresList)
        return sublistOfFeatures
    
    def getScoresForTrueFeatures(self,trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest) :
        forest = RandomForestClassifier(n_estimators = 100)
        XTrain=trueFeaturesForTrain+falseFeaturesForTrain
        labels=[1]*self.sizeOfTrainList+[0]*self.sizeOfTrainList
        forest = forest.fit(XTrain,labels)
        resultForCurrentDriver=forest.predict(trueFeaturesForTest)
        resultForOthers=forest.predict(falseFeaturesForTest)
        for element in resultForCurrentDriver:
            if (element==0) : self.FalseNegative+=1
            else : self.TruePositive+=1
        for element in resultForOthers:
            if (element==0) : self.TrueNegative+=1
            else : self.FalsePositive+=1
        return list(resultForCurrentDriver)
