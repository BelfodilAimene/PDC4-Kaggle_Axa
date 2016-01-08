import time
from source.model.Trace import Trace
from source.model.Driver import Driver
from source.exploratory.Exploration import *
from source.controller.featureExtractors.SimpleFeatureExtractor import *
from source.utils.Utils import *
def exploreOne(sourcePath="Drivers/16/13.csv") :

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
    sample_spacing=1

    #getSTFT(signal,sample_spacing=sample_spacing)
    #showFFT(signal,sample_spacing=sample_spacing)
    #showSpectrogramAmp(signal,sample_spacing=sample_spacing)
    
    print getMaximalFrequencies(signal,sample_spacing=sample_spacing,slidingWindowSize=20, stepSize=10,numberOfFrequency=3)
    

def exploreDriver(sourcePath="Drivers/16") :
    driver=Driver(sourcePath)
    driver.loadTraces()
    plotBoxPlotTracesSpeeds(driver)
    

def essayer() :
    l=[0,1,0,1,0,1,1,1,1,1]
    t,f,spectrogram=getSTFT(l,1,4,2)
    print t
    print f
    print spectrogram
    print getMaximalFrequencies(l,1,3,2)

exploreOne()
#exploreDriver()
#essayer()



