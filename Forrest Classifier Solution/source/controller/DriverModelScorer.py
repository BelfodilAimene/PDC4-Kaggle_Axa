import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
# le test se fait sur chaque 50 elements, car listOfFalseTracesFeatures contient 200 (150 pour entrainement et 50 pour test) donc l'entrainement doit contenir aussi 150
class DriverModelScorer :

    def __init__(self,oneDriverFeatures,listOfFalseTracesFeatures) :
        self.oneDriverFeatures=oneDriverFeatures
        self.listOfFalseTracesFeatures=listOfFalseTracesFeatures
        self.TruePositive=0
        self.TrueNegative=0
        self.FalsePositive=0
        self.FalseNegative=0
    def getScores(self) :
        
        scoresList=[]
        falseFeaturesForTrain=self.listOfFalseTracesFeatures[0:150]
        falseFeaturesForTest=self.listOfFalseTracesFeatures[150:200]

        # etape 1 pour les 50 premiers elements
        trueFeaturesForTrain=self.extractFeatures(50,200)
        trueFeaturesForTest=self.extractFeatures(0,50)
        scoresList+=self.getScoresFor50TrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest)

        # etape 2 pour les 50 2eme elements
        trueFeaturesForTrain=self.extractFeatures(0,50)
        trueFeaturesForTrain+=self.extractFeatures(100,200)
        trueFeaturesForTest=self.extractFeatures(50,100)
        scoresList+=self.getScoresFor50TrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest)

        # etape 3 pour les 50 3eme elements
        trueFeaturesForTrain=self.extractFeatures(0,100)
        trueFeaturesForTrain+=self.extractFeatures(150,200)
        trueFeaturesForTest=self.extractFeatures(100,150)
        scoresList+=self.getScoresFor50TrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest)

        # etape 4 pour les 50 4eme elements
        trueFeaturesForTrain=self.extractFeatures(0,150)
        trueFeaturesForTest=self.extractFeatures(150,200)
        scoresList+=self.getScoresFor50TrueFeatures(trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest)

        #print "evaluation :"
        #print self.TruePositive
        #print self.TrueNegative
        #print self.FalsePositive
        #print self.FalseNegative
        #print "end"
        for i in range(200) :
            scoresList.append(1)
        return scoresList
    

    def extractFeatures(self,minValue,maxValue) :
        sublistOfFeatures=[]
        for i in range(minValue,maxValue) :
            traceName,featuresList=self.oneDriverFeatures[i]
            sublistOfFeatures.append(featuresList)
        return sublistOfFeatures


    def getScoresFor50TrueFeatures(self,trueFeaturesForTrain,falseFeaturesForTrain,trueFeaturesForTest,falseFeaturesForTest) :
        forest = RandomForestClassifier(n_estimators = 100)
        XTrain=trueFeaturesForTrain+falseFeaturesForTrain
        labels=[1]*150
        labels+=[0]*150
        forest = forest.fit(XTrain,labels)
        resultForCurrentDriver=forest.predict(trueFeaturesForTest)
        resultForOthers=forest.predict(falseFeaturesForTest)
        for element in resultForCurrentDriver:
            if (element==0) :
                self.FalseNegative+=1
            else :
                self.TruePositive+=1
        for element in resultForOthers:
            if (element==0) :
                self.TrueNegative+=1
            else :
                self.FalsePositive+=1
        #print "lhagna"
        #print resultForCurrentDriver
        #print resultForOthers
        return list(resultForCurrentDriver)

























