import math,cmath
import numpy as np
from numpy.fft import rfftfreq,rfft
import matplotlib.pyplot as plt

#----------------------------------------------------------------------

def getFFT(signal, sampling_rate=1) :
    """
    get (frequency, complex coefficient) list representing the spectrum of the signal (list of value sampled with the sampling_rate (every 1s))
    """
    return zip(rfftfreq(len(signal),d=sampling_rate),rfft(signal))

def getSTFT(signal, sampling_rate=1, slidingWindowSize=20, stepSize=10) :
    
    return zip(rfftfreq(len(signal),d=sampling_rate),rfft(signal))

#----------------------------------------------------------------------

def showFFT(signal,sampling_rate=1) :
    """
    the signal is list of values sampeled with the sampling_rate (ex : 1s)
    show the signal, amplitude spectrum, phase spectrum
    """
    plt.figure(1)
    plt.clf()
    xList,yList=zip(*getFFT(signal,sampling_rate=sampling_rate))
    histoWidth=float("inf")
    for i in range(len(xList)-1) : histoWidth=min(histoWidth,xList[i+1]-xList[i])
    histoWidth*=0.3

    #Time serie
    ax=plt.subplot(311)
    amp=[abs(c) for c in yList]
    times=[sampling_rate*i for i in range(len(signal))]
    plt.plot(times,signal, '-',color="blue")
    plt.xlabel("time")
    plt.ylabel("Time serie")
    
    #Amplitude
    ax=plt.subplot(312)
    amp=[abs(c) for c in yList]
    plt.bar(xList,amp,width=histoWidth,color="green",edgecolor="green")
    plt.xlabel("Frequency (FFT)")
    plt.ylabel("Amplitude")

    #phase
    ax=plt.subplot(313)
    phase=[cmath.phase(c) for c in yList]
    plt.bar(xList,phase,width=histoWidth,color="red",edgecolor="red")
    plt.xlabel("Frequency (FFT)")
    plt.ylabel("Phase")

    plt.show()
    
#----------------------------------------------------------------------
