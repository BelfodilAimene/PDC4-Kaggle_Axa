import os,random
from SimpleFeatureExtractor import *
from DriverModelScorer import *
from ..model.Driver import Driver

DRIVER_NUMBER_PAGING=400 #The number of driver charged in memory simultaneously


class AllDriverTrajectoriesScorer :
    def __init__(self,driverRepositoryPath,outputCSVFilePath) :
        self.driverRepositoryPath=driverRepositoryPath
        self.outputCSVFilePath=outputCSVFilePath

        self.TruePositive=0
        self.TrueNegative=0
        self.FalsePositive=0
        self.FalseNegative=0

    def ouptutAllScores(self) :
        driverPaths=os.listdir(self.driverRepositoryPath)
        driverPaths.sort(key=lambda dirName : int(dirName))
        allScores=[]

        # La liste suivante contient pour chaque driver un tableau de tripsFeatures, un tripsFeature contient pour chacune des
        # 200 trips (le nom de du dossier du conducteur, un tableau de features)

        driversFeatures=[]
        curD=0
        allScores=[]
        print "Feature extraction : "
        for driverPath in driverPaths :
            print "\tCurrent driver :",curD
            path=os.path.join(self.driverRepositoryPath,driverPath)
            driver=Driver(path)
            driversFeatures.append((driver.driverName,self.getFeaturesOfDriver(driver.getTraces())))
            curD+=1
            
            if (curD%DRIVER_NUMBER_PAGING==0) :
                allScores.extend(self.processScores(driversFeatures))
                driversFeatures=[]
        if (len(driversFeatures)!=0) :
            allScores.extend(self.processScores(driversFeatures))
            driversFeatures=[]

        #-----------------------------------------------------------------------------------------------------
        #    Classification Evaluation
        #-----------------------------------------------------------------------------------------------------
        print "-"*50
        print "Classification evaluation :"
        print "\tTP :",self.TruePositive,"."
        print "\tTN :",self.TrueNegative,"."
        print "\tFP :",self.FalsePositive,"."
        print "\tFN :",self.FalseNegative,"."
        print "\tPrecision :",float(self.TruePositive)/float((self.TruePositive+self.FalsePositive)),"."
        print "\tRecall :",float(self.TruePositive)/float((self.TruePositive+self.FalseNegative)),"."
        print "-"*50
        #-----------------------------------------------------------------------------------------------------

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
        for i in range(100): result.append(sortedSignal[int(sizeOfSignal*i/100)])
        return result
                               
    def processScores(self,driversFeatures) :
        i=0
        numberOfFalseTraces=200
        allScores=[]
        print "Scoring traces :"
        for driverName, oneDriverFeatures in driversFeatures :
            print "\tCurrent driver :",i
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
