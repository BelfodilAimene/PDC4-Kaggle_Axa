from abc import ABCMeta, abstractmethod

class Scorer(object) :
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getScores(self,featureMapsList) :
        """
        input :
           featureMapsList : list of pair (traceName, featureMap)
        output :
           scores : list of scores (traceName, score)
        """
        pass
