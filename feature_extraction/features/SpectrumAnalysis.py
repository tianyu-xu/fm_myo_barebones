import pylab as pl
import numpy as np
import csv


from IIRFilter import LowPassIIR

# This is to determine the frequency range of the interference

def main():

    with open('emg.csv','r') as f:
        reader = csv.reader(f)
        data = [row[4] for row in reader]
        data = list(map(float,data))

    fs = 2000
    t = [x/2000.0 for x in range(2000)]

    # original signal
    pl.subplot(221)
    pl.plot(t,data)
    pl.xlabel('time(s)')
    pl.title("original signal")

    # Sampling points
    N = len(t)
    # Resolution
    df = fs/(N-1)
    # Build frequency array
    f = [df*n for n in range(0,N)]
    Y = np.fft.fft(data)*2/N
    # *2/N reflects the relationship between the result of
    # FFT transformation and the actual signal amplitude
    absY = [np.abs(x) for x in Y]
    # Plot fft before filter
    pl.subplot(223)
    pl.plot(f,absY)
    pl.xlabel('freq(Hz)')
    pl.title("fft before filter")
    pl.ylim((0,10))

    # filter
    IIR = LowPassIIR(a=0.7, y=data)
    data_fil = IIR.filter(data)

    pl.subplot(222)
    pl.plot(t,data_fil)
    pl.xlabel('time(s)')
    pl.title("signal after filter")
    N = len(t)
    df = fs/(N-1)
    f = [df*n for n in range(0,N)]
    Y = np.fft.fft(data_fil)*2/N
    absY = [np.abs(x) for x in Y]
    pl.subplot(224)
    pl.plot(f,absY)
    pl.xlabel('freq(Hz)')
    pl.title("fft after filter")
    pl.ylim((0,10))
    pl.show()

if __name__ == '__main__':
    main()


