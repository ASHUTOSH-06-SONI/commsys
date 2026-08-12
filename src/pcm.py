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

plt.figure(figsize=(10, 5))
plt.plot(t[:50], m[:50], label="Original Signal")
plt.step(t[:50], pcm_rec[:50], where="mid", label="PCM Reconstructed")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("PCM Reconstruction")
plt.legend()
plt.grid()
plt.show()