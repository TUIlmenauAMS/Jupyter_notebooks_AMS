import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

rate, snd = wav.read("sndfile.wav")
plt.hist(snd/(2.0**15),50)