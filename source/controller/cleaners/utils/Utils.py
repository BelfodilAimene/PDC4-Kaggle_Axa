import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
#        Mean Filter on feature
#------------------------------------------------------------------------------
def meanFilter(signal,windowSize=5) :
    totalValuesNumber=len(signal)
    cleanedSignal=[]
    lesserI=-(windowSize/2)
    upperI=min((windowSize+1)/2,len(signal))
    sumOfWindow=sum(signal[0:upperI])
    realSize=upperI
    
    for i in range(totalValuesNumber) :
        cleanedSignal.append(sumOfWindow/realSize)
        lesserI+=1
        upperI+=1
        if (lesserI>0) :
            sumOfWindow-=signal[lesserI-1]
            realSize-=1
        if (upperI<=totalValuesNumber) :
            sumOfWindow+=signal[upperI-1]
            realSize+=1
    return cleanedSignal

def medianFilter(signal,windowSize=5) :
    totalValuesNumber=len(signal)
    cleanedSignal=[]
    lesserI=-(windowSize/2)
    upperI=min((windowSize+1)/2,len(signal))

    window=signal[0:upperI]
    realSize=upperI
    
    for i in range(totalValuesNumber) :
        sortedWindow=sorted(window)
        cleanedSignal.append(sortedWindow[realSize/2])
        lesserI+=1
        upperI+=1
        if (lesserI>0) :
            window.pop(0)
            realSize-=1
        if (upperI<=totalValuesNumber) :
            window.append(signal[upperI-1])
            realSize+=1
    return cleanedSignal


#------------------------------------------------------------------------------
#        Plot Mean Filter on feature
#------------------------------------------------------------------------------
def showSignalMeanAndMedianFiltering(signal,WindowSize=60) :
    meanSignal=meanFilter(signal,WindowSize)
    medianSignal=medianFilter(signal,WindowSize)
    plt.figure(1)
    plt.clf()
    plt.subplot(311)
    plt.title('Duree du signal : {0}s'.format(len(signal)))
    plt.plot(range(len(signal)),signal, '-b')
    plt.xlabel("t (s)")
    plt.ylabel("signal")
    plt.subplot(312)
    plt.plot(range(len(meanSignal)),meanSignal, '-g')
    plt.ylabel("mean filter on signal")
    plt.subplot(313)
    plt.plot(range(len(medianSignal)),medianSignal, '-r')
    plt.ylabel("median filter on signal")
    plt.show()
#------------------------------------------------------------------------------
