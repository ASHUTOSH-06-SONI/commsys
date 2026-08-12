import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq
from scipy.signal import butter, sosfiltfilt

#Single tone amplitude modulation
Am = 1
Ac = 2
fm = 100
fc = 2000
mu = 0.8
fs = 10000
t = np.arange(0, 0.05, 1/fs)
m_t = Am * np.cos(2*np.pi*fm*t)
c_t = Ac * np.cos(2*np.pi*fc*t)
u_t = Ac * (1 + mu*m_t/Am) * np.cos(2*np.pi*fc*t)

#single tone demodulation
rectified = np.abs(u_t)
f_cutoff = 300
order = 5
sos = butter(order, f_cutoff,btype= 'low', fs = fs, output = 'sos')
filtered = sosfiltfilt(sos, rectified)
demod = filtered - np.mean(filtered)

"""
Inference from Plot 1- Range for Envelope = [2(1-0.8),2(1+0.8)] = [0.4,3.6]
Inference from Plot 2- Since we do np.abs(), the -ve half cycle gets flipped upwards
The envelope is still there, but there's a ton of high-frequency stuff riding on top of it.
To clean that stuff, we use Low pass filter
Inference from Plot 3- Recovered amplitude is approximately: +-1.04 (some component coz butterworth filter)
moreover, the signal we needed, that is m_t = Am*cos(2pi*fm*t), we get it coz Am = 1
"""
plt.subplot(3,1,1)
plt.plot(t[:750], u_t[:750])
plt.title("AM Signal")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t[:750], rectified[:750])
plt.title("Rectified")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t[50:450], demod[50:450])
plt.title("Demodulated")
plt.grid()
plt.tight_layout()
plt.show()

#Converting to frequency domain
n = len(m_t)
freq = fftfreq(n, d=1/fs)
pos = freq>=0
m_f = np.abs(fft(m_t))/n
c_f = np.abs(fft(c_t))/n
u_f = np.abs(fft(u_t))/n
d_f = np.abs(fft(demod))/n

plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.plot(freq[pos], m_f[pos])
plt.title("Message Spectrum")
plt.xlim(0, 2500)
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(freq[pos], c_f[pos])
plt.title("Carrier Spectrum")
plt.xlim(0, 2500)
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(freq[pos], u_f[pos])
plt.title("AM Spectrum")
plt.xlim(0, 2500)
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(freq[pos], d_f[pos])
plt.title("Demodulated Spectrum")
plt.xlim(0, 2500)
plt.grid()

plt.tight_layout()
plt.show()

print("Bandwidth = ", 2*fm," Hz")
print("Message Signal power = ",np.mean(m_t**2))
print("Carrier Signal power = ",np.mean(c_t**2))
print("Amplitude Modulated Signal power = ",np.mean(c_t**2)*(1+(mu**2)/2))