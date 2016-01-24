import ntpath
from Event import Event

class Trace :
    def __init__(self,filePath) :
        self.filePath=filePath;
        self.traceName=ntpath.basename(filePath).split(".")[0];
        self.trace=[]
        
    def loadTrace(self) :
        self.trace=[]
        i=0
        with open(self.filePath) as f:
            f.readline() #pour le header
            for line in f:
                line = line.strip().split(",") #x,y
                self.trace.append(Event(i,float(line[0]),float(line[1])))
                i+=1
                
    def getTrace(self) :
        if (not self.trace) :
            self.loadTrace()
        return self.trace

    def getPathDistance(self) :
        d=0
        lastEvent=None
        for event in self.trace :
            if lastEvent : d+=event.distance(lastEvent)
            lastEvent=event
        return d

    def getPathTime(self) :
        if (not self.trace) : return 0
        else : return self.trace[-1].t
            
            
    #----------------------------------------------------------
    #   Trace is seen as list of events
    #----------------------------------------------------------
    def __len__(self) :
        return len(self.trace)

    def __iter__(self):
        return iter(self.trace)

    def __getitem__(self,index):
        return self.trace[index]

    #----------------------------------------------------------
    def __str__(self) :
        return "{0}".format(self.traceName)
