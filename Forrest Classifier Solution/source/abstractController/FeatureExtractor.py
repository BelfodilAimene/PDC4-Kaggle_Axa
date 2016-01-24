from abc import ABCMeta, abstractmethod

class FeatureExtractor :
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getFeatureMap(self,trace) :
        """
        input :
           trace : list of event 
        output :
           featureMap : feature matrix
        """
        pass
