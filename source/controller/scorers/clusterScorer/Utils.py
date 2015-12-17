import math,cmath
import numpy as np
from numpy.fft import rfftfreq,rfft
import matplotlib.pyplot as plt
from ....abstractController.Scorer import Scorer

#----------------------------------------------------------------------

def getSpectrum(signal) :
    """
    get (complex coefficient, frequency) list representing the spectrum of the signal 
    """
    return sorted(zip(rfft(signal),rfftfreq(len(signal),d=1)),key=lambda e : -abs(e[0]))

#----------------------------------------------------------------------

def showSpectrum(times,signal) :
    """
    times and signal are parallet vector, for each instant in <times> vector, <signal> give the amplitude of the signal
    """
    plt.figure(1)
    plt.clf()
    yList,xList=zip(*getSpectrum(signal))
    sortedXList=sorted(xList)
    d=float("inf")
    for i in range(len(sortedXList)-1) : d=min(d,sortedXList[i+1]-sortedXList[i])

    #Time serie
    ax=plt.subplot(311)
    amp=[abs(c) for c in yList]
    plt.plot(times,signal, '-',color="blue")
    plt.xlabel("time")
    plt.ylabel("Time serie")
    
    #Amplitude
    ax=plt.subplot(312)
    amp=[abs(c) for c in yList]
    plt.bar(xList,amp,width=d*0.3,color="green",edgecolor="green")
    plt.xlabel("Frequency (FFT)")
    plt.ylabel("Amplitude")

    #phase
    ax=plt.subplot(313)
    phase=[cmath.phase(c) for c in yList]
    plt.bar(xList,phase,width=d*0.3,color="red",edgecolor="red")
    plt.xlabel("Frequency (FFT)")
    plt.ylabel("Phase")

    plt.show()
    
#----------------------------------------------------------------------
