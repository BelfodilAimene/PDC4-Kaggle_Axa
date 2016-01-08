import math,cmath
import numpy as np
from numpy.fft import rfftfreq,rfft
import matplotlib.pyplot as plt
from ....abstractController.Scorer import Scorer

class ClusterScorer(Scorer) :
    def getScores(self,featureMapsList) :
        scoresList=[]
        for traceName,featureMap in featureMapsList :
            print featureMap
        return np.array(scoresList)
