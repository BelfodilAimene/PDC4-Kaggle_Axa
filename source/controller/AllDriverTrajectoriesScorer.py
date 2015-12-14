import os
from DriverTrajectoriesScorer import DriverTrajectoriesScorer
from cleaners.NoCleaner import NoCleaner
from featureExtractors.SimpleFeatureExtractor import SimpleFeatureExtractor
from normalizers.NoNormalizer import NoNormalizer
from scorers.NoScorer import NoScorer

class AllDriverTrajectoriesScorer :
    def __init__(self,driverRepositoryPath,outputCSVFilePath) :
        self.driverRepositoryPath=driverRepositoryPath
        self.outputCSVFilePath=outputCSVFilePath
        self.cleaner=NoCleaner()
        self.featureExtractor=SimpleFeatureExtractor()
        self.normalizer=NoNormalizer()
        self.scorer=NoScorer()

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
        driverTrajectoriesScorer=DriverTrajectoriesScorer(self.cleaner,self.featureExtractor,self.normalizer,self.scorer)
        driverPaths=os.listdir(self.driverRepositoryPath)
        driverPaths.sort(key=lambda dirName : int(dirName))

        allScores=[]
        for driverPath in driverPaths :
            path=os.path.join(self.driverRepositoryPath,driverPath)
            scores=driverTrajectoriesScorer.scoreDriverTrajectories(path)
            allScores.extend(scores)

        csvFile=open(self.outputCSVFilePath, 'w')
        csvFile.write("driver_trip"+","+"prob"+"\n")
        for driver_trip,prob in allScores :
            line="{0},{1}\n".format(driver_trip,prob)
            csvFile.write(line)
        csvFile.close();

        
        
        
