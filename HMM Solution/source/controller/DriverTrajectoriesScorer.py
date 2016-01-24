from ..model.Driver import Driver

class DriverTrajectoriesScorer :
    def __init__(self,cleaner,featureExtractor,normalizer,scorer) :
        self.cleaner=cleaner
        self.featureExtractor=featureExtractor
        self.normalizer=normalizer
        self.scorer=scorer
        
    def scoreDriverTrajectories(self,directoryPath) :
        driver=Driver(directoryPath)
        driver.loadTraces()

        featureMaps=[]
        for trace in driver :
            trace=self.cleaner.clean(trace)
            featureMap=self.featureExtractor.getFeatureMap(trace)
            featureMaps.append((trace.traceName,featureMap))

        featureMaps=self.normalizer.normalize(featureMaps)
        scores=self.scorer.getScores(featureMaps)

        sortedScores=sorted(scores,key=lambda element : int(element[0]))
        sortedScores=map(lambda element : (driver.driverName+"_"+element[0],element[1]),sortedScores)

        return sortedScores
        
