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
    #showFFT(signal,sample_spacing=sample_spacing)
    showSpectrogramAmp(signal,sample_spacing=sample_spacing)
    #getSTFT(signal,sample_spacing=sample_spacing)

def exploreDriver(sourcePath="Drivers/16") :
    driver=Driver(sourcePath)
    driver.loadTraces()
    plotBoxPlotTracesSpeeds(driver)
    
    
exploreOne()
#exploreDriver()
"""
l=[0,1,2,3,4,5,6]

t,f,spectrogram=getSTFT(l,1,3,2)
print t
print f
print spectrogram
"""

