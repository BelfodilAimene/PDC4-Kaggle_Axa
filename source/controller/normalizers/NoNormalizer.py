from ...abstractController.Normalizer import Normalizer

class NoNormalizer(Normalizer) :
    def normalize(self,featureMap) :
        return featureMap
