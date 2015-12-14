from abc import ABCMeta, abstractmethod

class Normalizer :
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def normalize(self,featureMap) :
        """
        input :
           featureMap : featureMap (feature matrix)
        output :
           featureMap : normalized feature map 
        """
        pass
