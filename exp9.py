#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
""" 
Created on Thu Sep 17 10:44:08 2026 
wapp to simulate the tx of binary antipodal signals via an AWGN channel 
detect the rx bits using a simple threshold detector 
if rx>=1 -> return 1 if rx<0 -> return 0 
calculate bit error rate by comparing the tx'ed and detected bits
repeat this simulation for diff snr values (0,2,4,6,8,10 dBs)
plot bit error rate vs snr
antipodal generation + awgn-> tx'ed bits detectors at rx end- 
they get the outputs and hence get the bit error rate
@author: santoshsoni 
"""
import numpy as np
import matplotlib.pyplot as plt
N = 10000
snr = [0,2,4,6,8,10]
ber = []
# tx
tx_bits = np.random.randint(0, 2, N)
tx_signal = 2 * tx_bits - 1
# awgn
for i in snr:
    linear_snr = 10**(i/10)
    noise_var = 1/linear_snr
    noise = np.sqrt(noise_var) * np.random.randn(N)
    rx = tx_signal + noise
    # threshold detector
    rx_bits = []
    for j in range(N):
        if rx[j] >= 0:
            rx_bits.append(1)
        else:
            rx_bits.append(0)
    # er
    errors = 0
    for j in range(N):
        if tx_bits[j] != rx_bits[j]:
            errors += 1
    bit_Errors = errors / N
    ber.append(bit_Errors)
    print(f"SNR = {i:2d} dB | Errors = {errors} | BER = {bit_Errors:.4f}")

plt.figure(figsize=(8, 6))
plt.plot(snr, ber, 'o-')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR Graph")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
plt.semilogy(snr, ber, 'o-')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR Graph but Y value is smol")
plt.grid(True)
plt.show()
