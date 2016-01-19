import math,numpy as np,matplotlib.pyplot as plt

#-----------------------------------------------------------
#      Plot Events and Feature
#-----------------------------------------------------------
def plotEvents(trace) :
    xList=np.array([event.x for event in trace])
    yList=np.array([event.y for event in trace])
    plt.figure(1)
    plt.clf()
    plt.plot(xList,yList, 'o', markerfacecolor='k',markeredgecolor='k', markersize=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Taille de la trace : {0}s'.format(len(trace)))
    plt.show()

def plotSignal(signal) :
    plt.figure(1)
    plt.clf()
    plt.plot(range(len(signal)),signal, '-', markerfacecolor='r',markeredgecolor='r', markersize=1)
    plt.xlabel("t (s)")
    plt.ylabel("feature")
    plt.title('Taille de la trace : {0}s'.format(len(signal)))
    plt.show()

def plotFeature(featureMap,n) :
    plotSignal([e.item((0,0)) for e in featureMap[:,n]])
    

#-----------------------------------------------------------
#      Plot Distributions as Box Plot
#-----------------------------------------------------------

def plotBoxPlotTracesDistance(driver) :
    plt.boxplot([trace.getPathDistance() for trace in driver])
    plt.show()

def plotBoxPlotTracesTime(driver) :
    plt.boxplot([trace.getPathTime() for trace in driver])
    plt.show()

def plotBoxPlotTracesSpeeds(driver) :
    speeds=[]
    labels=[]
    for trace in driver :
        traceSpeed=[]
        lastEvent=None
        for event in trace :
            if (lastEvent) : traceSpeed.append(event.distance(lastEvent)/event.delai(lastEvent))
            lastEvent=event
        labels.append(trace.traceName)
        speeds.append(traceSpeed)
    plt.boxplot(speeds,labels=labels)
    plt.show()

#-----------------------------------------------------------

