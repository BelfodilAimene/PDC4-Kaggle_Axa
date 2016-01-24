from ...abstractController.Normalizer import Normalizer

class NoNormalizer(Normalizer) :
    def normalize(self,featureMapsList) :
        return featureMapsList
