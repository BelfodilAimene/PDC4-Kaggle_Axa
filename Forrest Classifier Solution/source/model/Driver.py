import ntpath
from Trace import Trace
import os

class Driver :
    def __init__(self,directoryPath) :
        self.directoryPath=directoryPath;
        head, tail = ntpath.split(directoryPath)
        self.driverName=tail or ntpath.basename(head)
        self.traces=[]
        
    def loadTraces(self) :
        tracesPaths=os.listdir(self.directoryPath)
        for tracePath in tracesPaths :
            path=os.path.join(self.directoryPath,tracePath)
            t=Trace(path)
            t.loadTrace()
            self.traces.append(t)
            
    def getTraces(self) :
        if (not self.traces) :
            self.loadTraces()
        return self.traces

    #----------------------------------------------------------
    #   Driver is seen as list of traces
    #----------------------------------------------------------
    def __len__(self) :
        return len(self.traces)

    def __iter__(self):
        return iter(self.traces)

    def __getitem__(self,index):
        return self.traces[index]

    #----------------------------------------------------------
    def __str__(self) :
        return "{0}".format(self.driverName)
