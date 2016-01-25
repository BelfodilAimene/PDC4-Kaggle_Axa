import numpy as np
from sklearn.ensemble import RandomForestClassifier

class DriverModelScorer :
    def __init__(self,oneDriverFeatures,listOfFalseTracesFeatures,crossValidationFoldSize=10,evaluateModel=True) :
        self.oneDriverFeatures=oneDriverFeatures
        self.listOfFalseTracesFeatures=listOfFalseTracesFeatures

        self.crossValidationFoldNumber=len(self.oneDriverFeatures)/crossValidationFoldSize
        self.sizeOfTestList=crossValidationFoldSize
        self.sizeOfTrainList=len(self.oneDriverFeatures)-self.sizeOfTestList

        self.evaluateModel=evaluateModel
        if (evaluateModel) :
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
            scoresList+=self.getScoresForTrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest,numberOfEstimator=100)
        
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
    
    def getScoresForTrueFeatures(self,trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest,numberOfEstimator=100) :
        forest = RandomForestClassifier(n_estimators = numberOfEstimator)
        XTrain=trueFeaturesForTrain+falseFeaturesForTrain
        labels=[1]*self.sizeOfTrainList+[0]*self.sizeOfTrainList
        forest = forest.fit(XTrain,labels)
        resultForCurrentDriverProba=forest.predict_proba(trueFeaturesForTest)
        resultForCurrentDriver=[row[1] for row in resultForCurrentDriverProba]
        resultForOthers=forest.predict(falseFeaturesForTest)

        #-----------------------------------------------------------------------------------------------------
        #    Information for evaluation update
        #-----------------------------------------------------------------------------------------------------
        if (self.evaluateModel) :
            for element in resultForCurrentDriver:
                if (element<0.5) : self.FalseNegative+=1
                else : self.TruePositive+=1
            for element in resultForOthers:
                if (element==0) : self.TrueNegative+=1
                else : self.FalsePositive+=1
        #-----------------------------------------------------------------------------------------------------

        return list(resultForCurrentDriver)
