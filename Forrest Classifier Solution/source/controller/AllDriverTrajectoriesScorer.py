import os,random
from SimpleFeatureExtractor import *
from DriverModelScorer import *
from ..model.Driver import Driver

DRIVER_NUMBER_PAGING=400 #The number of driver loaded in memory simultaneously


class AllDriverTrajectoriesScorer :
    def __init__(self,driverRepositoryPath,outputCSVFilePath,crossValidationFoldSize=10,evaluateModel=True) :
        self.driverRepositoryPath=driverRepositoryPath
        self.outputCSVFilePath=outputCSVFilePath

        self.crossValidationFoldSize=crossValidationFoldSize
        self.evaluateModel=evaluateModel
        if (evaluateModel) :
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
        currentDriverIndex=0
        allScores=[]
        print "Feature extraction : "
        for driverPath in driverPaths :
            print "\tCurrent driver :",currentDriverIndex
            path=os.path.join(self.driverRepositoryPath,driverPath)
            driver=Driver(path)
            driversFeatures.append((driver.driverName,self.getFeaturesOfDriver(driver.getTraces())))
            currentDriverIndex+=1
            
            if (currentDriverIndex%DRIVER_NUMBER_PAGING==0) :
                allScores.extend(self.processScores(driversFeatures))
                driversFeatures=[]
        if (len(driversFeatures)!=0) :
            allScores.extend(self.processScores(driversFeatures))
            driversFeatures=[]

        
        #-----------------------------------------------------------------------------------------------------
        #    Classification Evaluation
        #-----------------------------------------------------------------------------------------------------
        if (self.evaluateModel) :
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
        featureExtractor=SimpleFeatureExtractor()
        for trace in traces : tracesFeatures.append((trace.traceName,featureExtractor.getFeatures(trace)))
        return tracesFeatures # this is oneDriverFeatures
                               
    def processScores(self,driversFeatures) :
        i=0
        allScores=[]
        print "Scoring traces :"
        for driverName, oneDriverFeatures in driversFeatures :
            print "\tCurrent driver :",i
            listOfFalseTracesFeatures=self.getListOfNotCurrentDriver(driversFeatures,i,len(oneDriverFeatures))
            driverModelScorer=DriverModelScorer(oneDriverFeatures,listOfFalseTracesFeatures,crossValidationFoldSize=self.crossValidationFoldSize,evaluateModel=self.evaluateModel)
            scoresValues=driverModelScorer.getScores()

            #-----------------------------------------------------------------------------------------------------
            #    Information for evaluation update
            #-----------------------------------------------------------------------------------------------------
            if (self.evaluateModel) :
                self.TruePositive+=driverModelScorer.TruePositive
                self.TrueNegative+=driverModelScorer.TrueNegative
                self.FalsePositive+=driverModelScorer.FalsePositive
                self.FalseNegative+=driverModelScorer.FalseNegative
            #-----------------------------------------------------------------------------------------------------

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
            if (falseDriverIndex>=currentDriverIndex) : falseDriverIndex+=1
            falseDriverName,falseDriverFeatures =driversFeatures[falseDriverIndex]
            falseTraceIndex=random.randint(0, len(falseDriverFeatures)-1)
            falseTraceName,falseTraceFeatures=falseDriverFeatures[falseTraceIndex]
            listOfFalseTraces.append(falseTraceFeatures)
        return listOfFalseTraces    
