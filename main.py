import time

from source.controller.AllDriverTrajectoriesScorer import AllDriverTrajectoriesScorer

from source.controller.cleaners.NoCleaner import NoCleaner
from source.controller.featureExtractors.SimpleFeatureExtractor import SimpleFeatureExtractor
from source.controller.normalizers.NoNormalizer import NoNormalizer
from source.controller.scorers.NoScorer import NoScorer

def main(sourcePath="Drivers2",outputPath="axa_Submission.csv") :

    staringTime=time.time()

    noCleaner=NoCleaner()
    simpleFeatureExtractor=SimpleFeatureExtractor()
    noNormalizer=NoNormalizer()
    noScorer=NoScorer()

    allDriverTrajectoriesScorer=AllDriverTrajectoriesScorer(sourcePath,outputPath)
    allDriverTrajectoriesScorer.setCleaner(noCleaner).setFeatureExtractor(simpleFeatureExtractor).setNormalizer(noNormalizer).setScorer(noScorer)
    allDriverTrajectoriesScorer.ouptutAllScores()
        
    elapsed_time=(time.time()-staringTime)

    print "-"*40
    print "End."
    print "Elapsed time : {0}s".format(elapsed_time)
    print "-"*40
    
main()
