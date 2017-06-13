"""Decodiert ein AM moduliertes Signal aus einem Sound File, with name in the argument
z.B.: python AMdecoderbitstring.py amfile.wav"""
#Gerald Schuller, Januar 2015
#with updated filters

import sound
import scipy
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2

CHUNK = 1024

print("filename=", sys.argv[1])
sndfile=sys.argv[1]
#sndfile="amfile.wav";
#sndfile="amfilegs.wav";
#sndfile="amrec.wav";

#read in sound file:
[AM, FS]=sound.wavread(sndfile)
#length of the sound:
lenAM=scipy.size(AM)

#compute the low pass filter coefficients,
#with 10 Hz cutoff frequency:
[b,a]=scipy.signal.iirfilter(2, 20.0/(FS/2),rp=60,btype='lowpass')
[w,H]=scipy.signal.freqz(b,a)
Ha=scipy.absolute(H)
fig=plt.figure()
#plt.plot(w,Ha)
#In dB on normalized frequency axis w:
plt.plot(w,20*np.log10(Ha))
plt.title('The frequence response of the low pass filter')
plt.xlabel('Normalized frequency (pi=Nyquist freq.)') 
plt.ylabel('Magnitude response (dB)')
plt.axis([0,3.15,-80, 5])



fig=plt.figure()
fig.canvas.set_window_title('Das AM Signal mit Clock- und Bit-Signal')
plt.plot(AM)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()
#Compute average power to remove silence:
p=scipy.signal.lfilter(b, a, scipy.power(AM,2));

print("Filter the bit component:");
#get the bit frequency component at 1 kHz by down mixing:
#sinus Traeger:
traegersin = scipy.sin(2*scipy.pi/FS*1000*scipy.arange(0,lenAM));
downmixAMbits_sin=(traegersin*AM)
#De-modulate by low pass filtering and taking abs value (bit and clock are always positive)
decAMbits_sin=scipy.signal.lfilter(b, a, downmixAMbits_sin);
#Cosinus Traeger:
traegercos = scipy.cos(2*scipy.pi/FS*1000*scipy.arange(0,lenAM));
downmixAMbits_cos=(traegercos*AM)
#De-modulate by low pass filtering and taking abs value (bit and clock are always positive)
decAMbits_cos=scipy.signal.lfilter(b, a, downmixAMbits_cos);
#Berechne betrag der komplexen Demodulation:
decAMbits= np.sqrt(decAMbits_sin**2+decAMbits_cos**2)

fig=plt.figure()
fig.canvas.set_window_title('Das demodulierte Bit Signal')
plt.plot(decAMbits)
plt.xlabel('Sample')
plt.ylabel('Value')

#get the clock frequency component at 2 kHz:
traegersin = scipy.sin(2*scipy.pi/FS*2000*scipy.arange(0,lenAM));
#donw mix, magnitude:
downmixAMclock_sin=(traegersin*AM)
print("filter the clock component")
#de-modulate by low pass filtering:
decAMclock_sin=scipy.signal.lfilter(b, a, downmixAMclock_sin);

traegercos = scipy.cos(2*scipy.pi/FS*2000*scipy.arange(0,lenAM));
#donw mix, magnitude:
downmixAMclock_cos=(traegercos*AM)
#de-modulate by low pass filtering:
decAMclock_cos=scipy.signal.lfilter(b, a, downmixAMclock_cos);
#Taking complec magnitude:
decAMclock=np.sqrt(decAMclock_sin**2+decAMclock_cos**2)


fig=plt.figure()
fig.canvas.set_window_title('Das demodulierte Clock Signal')
plt.plot(decAMclock)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

#Schwelle zwischen 0 und 1 fuer die clock:
schwellec=max(decAMclock)/2.0;

#Shwelle zwische 0 und 1 fuer die bits:
schwelle=max(decAMbits)/2.0;
print("schwelle=", schwelle)
#Laenge des empfangenen geglaetteten Signals:
laenge=max(decAMbits.shape)

fig=plt.figure()
plt.plot((decAMbits>schwelle)*1.1-0.01,'r')
#fig=plt.figure()
plt.plot((decAMclock> schwellec),'b')
#plt.axis([0,10000 , -0.1, 1.1])
plt.title('Bits und Clock nach Schwellen-Operator')
plt.legend(('Bit-Signal nach Schwelle', 'Clock-Signal nach Schwelle'))
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

#Decodieren der Bits:
print("Decodieren der Bits:");
#Abtast-Intervall fuer geglaetetes Signal:
interv=40;
#Bitcounter:
m=0; 
#Bit-array:
bitstring='';
for n in range(interv,laenge,interv):
  #bei ueberschreiten der Schwelle des clock signales lese Bt aus:
  if ((decAMclock[n-interv] > schwellec) and  (decAMclock[n]< schwellec) ):
    #Auslesen des bits:
    print("clock detected at sample:",n)
    if (decAMbits[n] > schwelle):
      print("Bit detected: 1");
      bitstring=bitstring+ '1';
    else:
      print("Bit detected: 0");
      bitstring=bitstring+ '0';
    m = m+1;

from writereadbits import writebinaryfile

print "decoded bitstring= ", bitstring
print "write to binary file"
writebinaryfile('AMdecoded.bin', bitstring)



