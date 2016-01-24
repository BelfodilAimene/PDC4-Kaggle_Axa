import time
import matplotlib.pyplot as plt

from source.model.Trace import Trace
from source.model.Driver import Driver

from source.controller.featureExtractors.SimpleFeatureExtractor import *
from source.controller.scorers.utils.Utils import *
from source.controller.cleaners.utils.Utils import *

from source.exploratory.Exploration import *

def exploreOne(sourcePath="../Data/Drivers/16/122.csv") :

    trace=Trace(sourcePath)
    trace.loadTrace()
    print "Distance :",trace.getPathDistance(),"m"
    print "Time :",trace.getPathTime(),"s"

    plotEvents(trace)

    featureExtractor=SimpleFeatureExtractor()
    featureMap=featureExtractor.getFeatureMap(trace)
    feature=SPEED
    windowSize=60
    signal=[e.item((0,feature)) for e in featureMap]
    showSignalMeanAndMedianFiltering(signal,windowSize)

def exploreDriver(sourcePath="Drivers/16") :
    driver=Driver(sourcePath)
    driver.loadTraces()
    plotBoxPlotTracesSpeeds(driver)
    
exploreOne()


