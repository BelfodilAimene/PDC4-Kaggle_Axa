import numpy as np

class Scorer :
    def getScores(self,featureMapsList) :
        """
        input :
           featureMapsList : list of pair (traceName, featureMap)
        output :
           scores : list of scores (traceName, score)
        """

        scoresList=[]
        for traceName,featureMap in featureMapsList :
            scoresList.append((traceName,1))
            

        return np.array(scoresList)
