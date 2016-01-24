from abc import ABCMeta, abstractmethod

class Normalizer :
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def normalize(self,featureMapsList) :
        """
        input :
           featureMapsList : list of pair (traceName, featureMap)
        output :
           featureMapsList : normalized feature Maps List 
        """
        pass
