from ..model.Driver import Driver
from Cleaner import Cleaner
from FeatureExtractor import FeatureExtractor
from Normalizer import Normalizer
from Scorer import Scorer

class DriverTrajectoriesScorer :
    def scoreDriverTrajectories(self,directoryPath) :
        driver=Driver(directoryPath)
        driver.loadTraces()

        cleaner=Cleaner()
        featureExtractor=FeatureExtractor()
        normalizer=Normalizer()
        scorer=Scorer()

        featureMaps=[]
        for trace in driver :
            trace=cleaner.clean(trace)
            featureMap=featureExtractor.getFeatureMap(trace)
            featureMap=normalizer.normalize(featureMap)
            featureMaps.append((trace.traceName,featureMap))

        scores=scorer.getScores(featureMaps)

        sortedScores=sorted(scores,key=lambda element : int(element[0]))
        sortedScores=map(lambda element : (driver.driverName+"_"+element[0],element[1]),sortedScores)

        return sortedScores
        
