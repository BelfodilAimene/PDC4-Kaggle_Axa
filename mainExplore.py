import time
from source.model.Trace import Trace
from source.model.Driver import Driver
from source.exploratory.Exploration import *
from source.controller.featureExtractors.SimpleFeatureExtractor import *
from source.utils.Utils import *
def exploreOne(sourcePath="Drivers/16/160.csv") :

    trace=Trace(sourcePath)
    trace.loadTrace()

    print trace.getPathDistance(),"m"
    print trace.getPathTime(),"s"

    #plotEvents(trace)

    featureExtractor=SimpleFeatureExtractor()
    featureMap=featureExtractor.getFeatureMap(trace)
    feature=SPEED
    
    #plotFeature(featureMap,feature)
    
    signal=[e.item((0,feature)) for e in featureMap]
    sampling_rate=1
    showFFT(signal,sampling_rate=sampling_rate)

def exploreDriver(sourcePath="Drivers/16") :
    driver=Driver(sourcePath)
    driver.loadTraces()
    plotBoxPlotTracesSpeeds(driver)
    
    
exploreOne()
#exploreDriver()
