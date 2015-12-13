import time

from source.controller.AllDriverTrajectoriesScorer import AllDriverTrajectoriesScorer

def main(sourcePath="Drivers2",outputPath="axa_Submission.csv") :

    staringTime=time.time()

    allDriverTrajectoriesScorer=AllDriverTrajectoriesScorer(sourcePath,outputPath)
    allDriverTrajectoriesScorer.ouptutAllScores()
        
    elapsed_time=(time.time()-staringTime)

    print "-"*40
    print "End."
    print "Elapsed time : {0}s".format(elapsed_time)
    print "-"*40
    
main()
