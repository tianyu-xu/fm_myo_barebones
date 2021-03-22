import pylab as pl
import numpy as np
import csv

# This is to determine the frequency range of the interference
# Channel 8 is the best to see the plot

def main():
    with open('emg.csv','r') as f:
        reader = csv.reader(f)
        data = [row[7] for row in reader]

    fs = 2000
    t = [x/2000.0 for x in range(2000)]
    # original signal
    pl.subplot(311)
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
    pl.subplot(312)
    pl.plot(f,absY)
    pl.xlabel('freq(Hz)')
    pl.title("fft")

    data2 = data[0:100]
    fs2 = 100
    t2 = [x/100.0 for x in range(100)]
    N2 = len(t2)
    df2 = fs2/(N2-1)
    f2 = [df2*n for n in range(0,N2)]
    Y2 = np.fft.fft(data2)*2/N2
    absY2 = [np.abs(x) for x in Y2]
    pl.subplot(313)
    pl.plot(f2,absY2)
    pl.xlabel('freq(Hz)')
    pl.title("fft")
    pl.show()


if __name__ == '__main__':
    main()


