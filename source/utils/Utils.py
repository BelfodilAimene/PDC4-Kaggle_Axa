import math,cmath
import numpy as np
from numpy.fft import rfftfreq,rfft
import matplotlib.pyplot as plt

#----------------------------------------------------------------------

def getFFT(signal, sample_spacing=1) :
    """
    get (frequency, complex coefficient) list representing the spectrum of the signal (list of value sampled with the sample_spacing (1/sample_rate) (every 1s))
    """
    return zip(rfftfreq(len(signal),d=sample_spacing),rfft(signal))

def getSTFT(signal, sample_spacing=1, slidingWindowSize=20, stepSize=10) :
    
    return zip(rfftfreq(len(signal),d=sample_spacing),rfft(signal))

#----------------------------------------------------------------------

def showFFT(signal,sample_spacing=1) :
    """
    the signal is list of values sampeled with the sampling_rate (ex : 1s)
    show the signal, amplitude spectrum, phase spectrum
    """
    plt.figure(1)
    plt.clf()
    xList,yList=zip(*getFFT(signal,sample_spacing=sample_spacing))
    histoWidth=float("inf")
    for i in range(len(xList)-1) : histoWidth=min(histoWidth,xList[i+1]-xList[i])
    histoWidth*=0.3

    #Time serie
    ax=plt.subplot(311)
    amp=[abs(c) for c in yList]
    times=[sample_spacing*i for i in range(len(signal))]
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
