import time,random
from source.controller.AllDriverTrajectoriesScorer import AllDriverTrajectoriesScorer

def main(sourcePath="../Data/Drivers",outputPath="axa_Submission.csv") :

    staringTime=time.time()

    random.seed(0)
    allDriverTrajectoriesScorer=AllDriverTrajectoriesScorer(sourcePath,outputPath,crossValidationFoldSize=10,evaluateModel=True)
    allDriverTrajectoriesScorer.ouptutAllScores()
    
    elapsed_time=time.time()-staringTime

    print "-"*50
    print "End",
    print "(Elapsed time : {0}s).".format(elapsed_time)
    print "-"*50
    
main()
