import math,cmath,numpy as np,matplotlib.pyplot as plt
from numpy.fft import rfftfreq,rfft

#----------------------------------------------------------------------
#         Fourier transform and Short-Time Fourier Transform
#----------------------------------------------------------------------
def getFFT(signal, sample_spacing=1) :
    """
    get (frequency, complex coefficient) list representing the spectrum of the signal (list of value sampled with the sample_spacing (1/sample_rate) (every 1s))
    """
    return zip(rfftfreq(len(signal),d=sample_spacing),rfft(signal))

def segmentSignal(signal, slidingWindowSize=20, stepSize=10) :
    """
    segment signal with slidingWindowSize=20 (number of sample in window) and stepSize=10 (number of samle to sample from window to another)
    """
    if (not signal) : return []
    
    numberOfSemgent=len(signal)/stepSize
    if (len(signal)%stepSize) : numberOfSemgent+=1
    segmented=[list() for _ in xrange(numberOfSemgent)]

    k=0
    lesserSegment=0
    upperSegment=-1
    
    for v in signal :
        if (k%stepSize==0) : upperSegment+=1  
        for i in xrange(lesserSegment,upperSegment+1) : segmented[i].append(v)
        if (len(segmented[lesserSegment])==slidingWindowSize) : lesserSegment+=1 
        k+=1
    last=numberOfSemgent-1
    while (len(segmented[last])<slidingWindowSize) :
        segmented[last]+=[0]*(slidingWindowSize-len(segmented[last]))
        last-=1
    return segmented
    

def getSTFT(signal, sample_spacing=1, slidingWindowSize=20, stepSize=10) :
    """
    Get short-time fourier transform with slidingWindowSize=20 (number of sample in window) and stepSize=10 (number of samle to sample from window to another)
    """
    segmentedSignal=segmentSignal(signal,slidingWindowSize,stepSize)
    segmentedSignalSTFT=[]
    for segment in segmentedSignal : segmentedSignalSTFT.append(rfft(segment))
    spectrogram=np.array(segmentedSignalSTFT)
    t=np.array([stepSize*i for i in xrange(len(segmentedSignal))])
    f=np.array(rfftfreq(slidingWindowSize,d=sample_spacing))
    return t,f,spectrogram

def getMaximalFrequencies(signal,sample_spacing=1, slidingWindowSize=20, stepSize=10,numberOfFrequency=1) :
    t,f,spectrogram=getSTFT(signal, sample_spacing=sample_spacing, slidingWindowSize=slidingWindowSize, stepSize=stepSize)
    f=[float(int(1000*freq))/1000 for freq in f]
    numberOfFrequency=min(numberOfFrequency,len(f))
    maximalFrequencies=[]
    for shortFFT in spectrogram :
        sortedFrequencies=zip(*sorted(zip(f,shortFFT),key = lambda element : abs(element[1]), reverse=True))[0]
        maximalFrequencies.append(list(sortedFrequencies[0:numberOfFrequency]))
    return maximalFrequencies

"""
from scipy import signal as scipySignalProcessing
def getSTFTWithScipy(signal,sample_spacing=1, slidingWindowSize=20, stepSize=10) :
    return scipySignalProcessing.spectrogram(signal,fs=1.0/sample_spacing,window=('boxcar', slidingWindowSize),nperseg=slidingWindowSize,noverlap=slidingWindowSize-stepSize,mode="psd")
"""    

#----------------------------------------------------------------------
#     plot signal and spectrum
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

def showSpectrogramAmp(signal, sample_spacing=1, slidingWindowSize=20, stepSize=10) :
    t,f,spectrogram=getSTFT(signal, sample_spacing=sample_spacing, slidingWindowSize=slidingWindowSize, stepSize=stepSize)
    spectrogram=zip(*spectrogram)
    amp=np.array([[abs(z) for z in l] for l in spectrogram])
    plt.pcolormesh(t, f, amp)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
#----------------------------------------------------------------------
