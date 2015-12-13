import os
from DriverTrajectoriesScorer import DriverTrajectoriesScorer

class AllDriverTrajectoriesScorer :
    def __init__(self,driverRepositoryPath,outputCSVFilePath) :
        self.driverRepositoryPath=driverRepositoryPath
        self.outputCSVFilePath=outputCSVFilePath
        self.driverTrajectoriesScorer=DriverTrajectoriesScorer()

    def ouptutAllScores(self) :
        driverPaths=os.listdir(self.driverRepositoryPath)
        driverPaths.sort(key=lambda dirName : int(dirName))

        allScores=[]
        for driverPath in driverPaths :
            path=os.path.join(self.driverRepositoryPath,driverPath)
            scores=self.driverTrajectoriesScorer.scoreDriverTrajectories(path)
            allScores.extend(scores)

        csvFile=open(self.outputCSVFilePath, 'w')
        csvFile.write("driver_trip"+","+"prob"+"\n")
        for driver_trip,prob in allScores :
            line="{0},{1}\n".format(driver_trip,prob)
            csvFile.write(line)
        csvFile.close();

        
        
        
