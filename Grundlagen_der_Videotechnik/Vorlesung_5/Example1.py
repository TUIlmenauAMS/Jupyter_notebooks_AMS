import numpy as np
import matplotlib.pyplot as plt



# DC Signal:
x = np.ones(32)

# Initialize downsampled signal:
xds = np.zeros(32)

# Downsample with M=4:
xds[0:32:4] = x[0:32:4]

# Plot both signals:
plt.plot(x)
plt.axis([0, 32, -0.1, 1.1])
plt.plot(xds)
plt.title('DC Signal (Blau) und mit N=4 unterabgetastete Version (Gruen)')
plt.xlabel('n')
plt.ylabel('x(n), xds(n)')
plt.show()

# Plotting the magnitude response of the original signal:

plt.plot(np.abs(np.fft.fft(x)))
plt.title('Betrag der DFT des Original DC Signals')
plt.xlabel('k')
plt.ylabel('abs(FFT(x))')
plt.show()

# Now we look at the magnitude response of the DFT of the undersampled version:
XDS = np.fft.fft(xds)
plt.plot(np.abs(XDS))
plt.title('Betrag der DFT der unterabgetasteten Version')
plt.xlabel('k')
plt.ylabel('abs(FFT(xds))')
plt.show()

# Now we test a signal with a higher frequency and apply the downsampling by M = 4 again:
x = np.sin(2 * np.pi / 32 * 3 * np.arange(32))
xds = np.zeros(32)
xds[0:32:4] = x[0:32:4]
plt.plot(x)
plt.plot(xds)
plt.title('x(n) (Blau), mit N=4 unterabgetastete Version xds(n) (Gruen)')
plt.show()

# The magnitude response of the original signal is:
plt.plot(np.abs(np.fft.fft(x)))
plt.title('Betrag der DFT des Original Sinus Signals')
plt.xlabel('k')
plt.ylabel('abs(FFT(x))')
plt.show()

# Now we plot the magnitude response of the downsampled signal:
XDS = np.fft.fft(xds)
plt.plot(np.abs(XDS))
plt.title('Betrag der DFT der unterabgetasteten Version')
plt.xlabel('k')
plt.ylabel('abs(FFT(xds))')
plt.show()

x = np.sin(2 * np.pi / 32 * 4 * np.arange(32))
xds = np.zeros(32)
xds[0:32:4] = x[0:32:4]
print(xds)
