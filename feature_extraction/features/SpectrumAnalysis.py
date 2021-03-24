import pylab as pl
import numpy as np
import csv
from IIRFilter import LowPassIIR

# This is to determine the frequency range of the interference
# Channel 8 is the best to see the plot

def main():

    IIR = LowPassIIR(a=0.7)

    with open('emg.csv','r') as f:
        reader = csv.reader(f)
        data = [row[7] for row in reader]

    fs = 2000
    t = [x/2000.0 for x in range(2000)]

    # filter
    for i in range(0,2000):
        data_fil = list(map(float,data))
        data_fil[i] = IIR.filter(data_fil[i])

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
    # the modulus of the Fourier transform result
    # Spectrum analysis
    pl.subplot(223)
    pl.plot(f,absY)
    pl.xlabel('freq(Hz)')
    pl.title("fft before filter")

    pl.subplot(222)
    pl.plot(t,data_fil)
    pl.xlabel('time(s)')
    pl.title("signal after filter")
    # Sampling points
    N = len(t)
    # Resolution
    df = fs/(N-1)
    # Build frequency array
    f = [df*n for n in range(0,N)]
    Y = np.fft.fft(data_fil)*2/N
    absY = [np.abs(x) for x in Y]
    pl.subplot(224)
    pl.plot(f,absY)
    pl.xlabel('freq(Hz)')
    pl.title("fft after filter")

    pl.show()

if __name__ == '__main__':
    main()


