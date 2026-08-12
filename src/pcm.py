import numpy as np
import matplotlib.pyplot as plt
fs = 600
T = 1
t = np.arange(0,T,1/fs)
m = 2*np.sin(2*np.pi*30*t)+ 4*np.cos(2*np.pi*60*t)

bits_pcm = 8
levels_pcm = 2**bits_pcm
xmin = np.min(m)
xmax = np.max(m)
del_pcm = (xmax - xmin) / (levels_pcm - 1)
#Encoder
indices = np.round((m - xmin) / del_pcm)
indices = np.clip(indices, 0, levels_pcm - 1)

#Decoder
pcm_rec = indices * del_pcm + xmin
pcm_mse = np.mean((m - pcm_rec)**2)
print("PCM MSE =", pcm_mse)

plt.subplot(2,1,1)
plt.plot(t[:50],m[:50])
plt.xlabel('time')
plt.ylabel('m(t)')

plt.subplot(2,1,2)
plt.plot(t[:50],pcm_rec[:50])
plt.xlabel('time')
plt.ylabel('reconstructed_signal')
