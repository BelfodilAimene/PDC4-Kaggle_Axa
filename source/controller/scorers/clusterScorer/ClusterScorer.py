import numpy as np
from ....abstractController.Scorer import Scorer

class ClusterScorer(Scorer) :
    def getScores(self,featureMapsList) :
        scoresList=[]
        for traceName,featureMap in featureMapsList :
            print featureMap
        return np.array(scoresList)
