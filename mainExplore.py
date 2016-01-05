import time
from source.model.Trace import Trace
from source.exploratory.Exploration import plotEvents,plotFeature
from source.controller.featureExtractors.SimpleFeatureExtractor import *
from source.controller.scorers.clusterScorer.Utils import getSpectrum,showSpectrum
def main(sourcePath="Drivers/16/103.csv") :
    featureExtractor=SimpleFeatureExtractor()
    trace=Trace(sourcePath)
    trace.loadTrace()
    #plotEvents(trace)
    featureMap=featureExtractor.getFeatureMap(trace)
    feature=BEARING
    plotFeature(featureMap,feature)
    

    #times,signal=zip(*[(e.item((0,0)),e.item((0,feature))) for e in featureMap])

    #showSpectrum(times,signal)
    
main()
