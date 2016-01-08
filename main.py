import time

from source.controller.AllDriverTrajectoriesScorer import AllDriverTrajectoriesScorer

from source.controller.cleaners.NoCleaner import NoCleaner
from source.controller.featureExtractors.SimpleFeatureExtractor import SimpleFeatureExtractor
from source.controller.normalizers.MinMaxNormalizer import MinMaxNormalizer
from source.controller.scorers.clusterScorer.ClusterScorer import ClusterScorer
from source.controller.scorers.HMM.HMMBasedScorer import HMMBasedScorer
def main(sourcePath="Drivers3",outputPath="axa_Submission.csv") :

    staringTime=time.time()

    noCleaner=NoCleaner()
    simpleFeatureExtractor=SimpleFeatureExtractor()
    minMaxNormalizer=MinMaxNormalizer()
    myScorer=ClusterScorer()

    allDriverTrajectoriesScorer=AllDriverTrajectoriesScorer(sourcePath,outputPath)
    allDriverTrajectoriesScorer.setCleaner(noCleaner).setFeatureExtractor(simpleFeatureExtractor).setNormalizer(minMaxNormalizer).setScorer(myScorer)
    allDriverTrajectoriesScorer.ouptutAllScores()
        
    elapsed_time=(time.time()-staringTime)

    print "-"*40
    print "End."
    print "Elapsed time : {0}s".format(elapsed_time)
    print "-"*40
    
main()
