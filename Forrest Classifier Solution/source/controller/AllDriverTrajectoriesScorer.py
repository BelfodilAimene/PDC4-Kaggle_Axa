import os
import random
#from DriverTrajectoriesScorer import DriverTrajectoriesScorer
from cleaners.NoCleaner import NoCleaner
from featureExtractors.SimpleFeatureExtractor import *
from scorers.ModelScorer.DriverModelScorer import *

#from normalizers.NoNormalizer import NoNormalizer
from scorers.NoScorer import NoScorer
from ..model.Driver import Driver

class AllDriverTrajectoriesScorer :
    def __init__(self,driverRepositoryPath,outputCSVFilePath) :
        self.driverRepositoryPath=driverRepositoryPath
        self.outputCSVFilePath=outputCSVFilePath
        self.cleaner=NoCleaner()
        self.featureExtractor=SimpleFeatureExtractor()
        #self.normalizer=NoNormalizer()
        self.scorer=NoScorer()
        self.TruePositive=0
        self.TrueNegative=0
        self.FalsePositive=0
        self.FalseNegative=0

    def setCleaner(self,cleaner) :
        self.cleaner=cleaner
        return self

    def setFeatureExtractor(self,featureExtractor) :
        self.featureExtractor=featureExtractor
        return self

    def setNormalizer(self,normalizer) :
        self.normalizer=normalizer
        return self

    def setScorer(self,scorer) :
        self.scorer=scorer
        return self
        
    def ouptutAllScores(self) :
        #driverTrajectoriesScorer=DriverTrajectoriesScorer(self.cleaner,self.featureExtractor,self.normalizer,self.scorer)
        driverPaths=os.listdir(self.driverRepositoryPath)
        driverPaths.sort(key=lambda dirName : int(dirName))
        allScores=[]
        # la liste suivante contient pour chaque driver un tableau de tripsFeatures, un tripsFeature contient pour chacune des
        # 200 trips (le nom de du dossier du monsieur, un tableau de features)
        driversFeatures=[]
        curD=0
        allScores=[]
        print "feature extraction"
        for driverPath in driverPaths :
            print "current driver :"
            print curD            
            path=os.path.join(self.driverRepositoryPath,driverPath)
            driver=Driver(path)
            driversFeatures.append((driver.driverName,self.getFeaturesOfDriver(driver.getTraces())))
            curD+=1
            if (curD%400==0) :
                allScores.extend(self.processScores(driversFeatures))
                driversFeatures=[]
        if (len(driversFeatures)!=0) :
            allScores.extend(self.processScores(driversFeatures))        
        print "evaluation :"
        print self.TruePositive
        print self.TrueNegative
        print self.FalsePositive
        print self.FalseNegative
        print "precision"
        print float(self.TruePositive)/float((self.TruePositive+self.FalsePositive))
        print "recall"
        print float(self.TruePositive)/float((self.TruePositive+self.FalseNegative))
        print "end"
        csvFile=open(self.outputCSVFilePath, 'w')
        csvFile.write("driver_trip"+","+"prob"+"\n")
        for driver_trip,prob in allScores :
            line="{0},{1}\n".format(driver_trip,prob)
            csvFile.write(line)
        csvFile.close();

    def getFeaturesOfDriver(self,traces) :
        tracesFeatures=[]
        for trace in traces :
            tracesFeatures.append((trace.traceName,self.getFeaturesOfTrace(trace)))
        return tracesFeatures # this is oneDriverFeatures
    def getFeaturesOfTrace(self,trace) :
        featureExtractor=SimpleFeatureExtractor()
        featureMap=featureExtractor.getFeatureMap(trace)
        featuresOfTrace=[]

        #percentiles=self.getPercentiles([row[0,DISTANCE] for row in featureMap])
        #print percentiles
        #featuresOfTrace+=percentiles
        
        percentiles=self.getPercentiles([row[0,SPEED] for row in featureMap])
        #print percentiles
        featuresOfTrace+=percentiles
        
        percentiles=self.getPercentiles([row[0,ACCELERATION] for row in featureMap])
        #print percentiles
        featuresOfTrace+=percentiles
        
        #percentiles=self.getPercentiles([row[0,BEARING] for row in featureMap])
        #print percentiles
        #featuresOfTrace+=percentiles
        
        percentiles=self.getPercentiles([row[0,ABSOLUTE_ANGULAR_VELOCITY] for row in featureMap])
        #print percentiles
        featuresOfTrace+=percentiles

        percentiles=self.getPercentiles([row[0,ANGULAR_ACCELERATION] for row in featureMap])
        #print percentiles
        featuresOfTrace+=percentiles
        
        return featuresOfTrace

    def getPercentiles(self, signal):
        sortedSignal=sorted(signal)
        result=[]
        sizeOfSignal=len(signal)
        for i in range(100):
            result.append(sortedSignal[int(sizeOfSignal*i/100)])
        return result
                               
    def processScores(self,driversFeatures) :
        i=0
        numberOfFalseTraces=200
        allScores=[]
        print "scoring"
        for driverName, oneDriverFeatures in driversFeatures :
            print "current Driver "
            print i
            listOfFalseTracesFeatures=self.getListOfNotCurrentDriver(driversFeatures,i,numberOfFalseTraces)
            driverModelScorer=DriverModelScorer(oneDriverFeatures,listOfFalseTracesFeatures)
            scoresValues=driverModelScorer.getScores()
            # update of evaluations
            self.TruePositive+=driverModelScorer.TruePositive
            self.TrueNegative+=driverModelScorer.TrueNegative
            self.FalsePositive+=driverModelScorer.FalsePositive
            self.FalseNegative+=driverModelScorer.FalseNegative
            scoresList=[]
            j=0
            for traceName,featuresList in oneDriverFeatures :    
                scoresList.append((traceName,scoresValues[j]))
                j+=1
            driverScore=np.array(scoresList)
            sortedScores=sorted(driverScore,key=lambda element : int(element[0]))
            sortedScores=map(lambda element : (driverName+"_"+element[0],element[1]),sortedScores)
            allScores.extend(sortedScores)
            i+=1
        return allScores




    def getListOfNotCurrentDriver(self,driversFeatures,currentDriverIndex,numberOfFalseTraces) :
        listOfFalseTraces=[]
        numberOfDrivers=len(driversFeatures)
        for i in range(numberOfFalseTraces) :
            falseDriverIndex=random.randint(0, numberOfDrivers-2)
            if (falseDriverIndex>=currentDriverIndex) :
                falseDriverIndex+=1
            falseTraceIndex=random.randint(0, 199)
            falseDriverName, falseDriverFeatures =driversFeatures[falseDriverIndex]
            falseTraceName,falseTraceFeatures=falseDriverFeatures[falseTraceIndex]
            listOfFalseTraces.append(falseTraceFeatures)
        return listOfFalseTraces














    
        
