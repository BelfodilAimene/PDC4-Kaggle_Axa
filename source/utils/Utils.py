import math,cmath
import numpy as np
from numpy.fft import rfftfreq,rfft
import matplotlib.pyplot as plt

#----------------------------------------------------------------------

def getFFT(signal) :
    """
    get (frequency, complex coefficient) list representing the spectrum of the signal 
    """
    return zip(rfftfreq(len(signal),d=1),rfft(signal))

def getSTFT(signal, slidingWindowSize=20, stepSize=10) :
    return zip(rfftfreq(len(signal),d=1),rfft(signal))

#----------------------------------------------------------------------

def showFFT(times,signal) :
    """
    times and signal are parallet vector, for each instant in <times> vector, <signal> give the amplitude of the signal
    """
    plt.figure(1)
    plt.clf()
    xList,yList=zip(*getFFT(signal))
    histoWidth=float("inf")
    for i in range(len(xList)-1) : histoWidth=min(histoWidth,xList[i+1]-xList[i])
    histoWidth*=0.3

    #Time serie
    ax=plt.subplot(311)
    amp=[abs(c) for c in yList]
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
