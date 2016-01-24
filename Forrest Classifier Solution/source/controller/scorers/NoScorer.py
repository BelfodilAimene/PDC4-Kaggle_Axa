import numpy as np
from ...abstractController.Scorer import Scorer

class NoScorer(Scorer) :
    def getScores(self,featureMapsList) :
        scoresList=[]
        for traceName,featureMap in featureMapsList :
            scoresList.append((traceName,1))
        return np.array(scoresList)
