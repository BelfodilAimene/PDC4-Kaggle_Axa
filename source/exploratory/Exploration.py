import math
import numpy as np
import matplotlib.pyplot as plt

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

def plotFeature(featureMap,n) :
    xList=[e.item((0,0)) for e in featureMap[:,0]]
    yList=[e.item((0,0)) for e in featureMap[:,n]]
    plt.figure(1)
    plt.clf()
    plt.plot(xList,yList, '-', markerfacecolor='r',markeredgecolor='r', markersize=1)
    plt.xlabel("t (s)")
    plt.ylabel("feature")
    plt.title('Taille de la trace : {0}s'.format(xList[-1]))
    plt.show()
