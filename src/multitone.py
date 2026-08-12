import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
a1,a2,a3 = 1,0.7,0.5
f1,f2,f3 = 100,300,500
fs = 10000
mu = 0.8
Ac = 2
fc = 2000
t = np.arange(0, 0.05, 1/fs)

c_t = Ac * np.cos(2*np.pi*fc*t)
m_t = a1*np.sin(2*np.pi*f1*t)+ a2*np.sin(2*np.pi*f2*t)+ a3*np.sin(2*np.pi*f3*t)
amp = np.max(np.abs(m_t))
u_t = Ac*(1 + mu*m_t/amp)*np.cos(2*np.pi*fc*t)
analytic_signal = hilbert(u_t)
envelope = np.abs(analytic_signal)
demodulated = (envelope/Ac - 1) * amp/mu

plt.figure(figsize=(10,8))
plt.subplot(4,1,1)
plt.title("Message signal")
plt.plot(t[:500],m_t[:500])
plt.grid()

plt.subplot(4,1,2)
plt.title("carrier signal")
plt.plot(t[50:450],c_t[50:450])
plt.grid()

plt.subplot(4,1,3)
plt.title("Envelope ")
plt.plot(t[50:450], envelope[50:450], label="Envelope")
plt.plot(t[50:450], Ac*(1 + mu*m_t/amp)[50:450], '--', label="Theoretical Envelope")
plt.legend()
plt.grid()

plt.subplot(4,1,4)
plt.title("Demodulated signal")
plt.plot(t[:500],demodulated[:500])
plt.grid()

plt.tight_layout()
plt.show()


n = len(m_t)
n = len(m_t)
freq = fftfreq(n, d=1/fs)
pos = freq>=0
m_f = np.abs(fft(m_t))/n
c_f = np.abs(fft(c_t))/n
u_f = np.abs(fft(u_t))/n
d_f = np.abs(fft(demodulated))/n

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

print("Bandwidth = ", 2*max(f1,f2,f3)," Hz")
print("Message Signal power = ",np.mean(m_t**2))
print("Carrier Signal power = ",np.mean(c_t**2))
print("Amplitude Modulated Signal power = ",np.mean(c_t**2)*(1+(mu**2)*np.mean(m_t**2)/amp**2))