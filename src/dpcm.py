
import numpy as np
import matplotlib.pyplot as plt

#sample
fs = 1200
T =1 
t = np.arange(0,T,1/fs)
m= 2*np.sin(2*np.pi*30*t)+ 4*np.cos(2*np.pi*60*t)

#predict
pred = np.zeros_like(m)
pred[0] = 0
pred[1] = m[0]
for n in range(2,len(m)):
    pred[n] = (m[n-1]+m[n-2])/2

#calculate error 
error = m-pred
print("Original range:", np.min(m),",", np.max(m))
print("Error range:", np.min(error), ",", np.max(error))

#quantize 
bits_dpcm = 8
levels_dpcm = 2**bits_dpcm

emin = np.min(error)
emax = np.max(error)
del_dpcm = (emax-emin)/(levels_dpcm-1)

#encoder encode each index as an 8-bit binary value
indices = np.round((error-emin)/del_dpcm)
indices = np.clip(indices,0,levels_dpcm-1)
encoded = [format(int(i), '08b') for i in indices]

#decode
error_rec = indices*del_dpcm+emin   #prediction error
reconstructed = np.zeros_like(m)
reconstructed[0] = error_rec[0]
reconstructed[1] = reconstructed[0]+error_rec[1]
for n in range(2,len(m)):
    pred = ((reconstructed[n-1]+reconstructed[n-2]))/2
    reconstructed[n] = pred + error_rec[n]
    
    
dpcm_mse = np.mean((m-reconstructed)**2)
print("DPCM MSE = ",dpcm_mse)

plt.figure(figsize=(10, 5))
plt.plot(t[:50], m[:50], label="Original Signal")
plt.step(t[:50], reconstructed[:50], where="mid", label="DPCM Reconstructed")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("DPCM Reconstruction")
plt.legend()
plt.grid()
plt.show()