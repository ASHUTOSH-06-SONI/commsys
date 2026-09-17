#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:47:03 2026
@author: santoshsoni
"""
import numpy as np
import matplotlib.pyplot as plt
N = 10000              
iterations = 50        
snr = [0,2,4,6,8,10]
avg_ber = []

# Monte Carlo simulation
for snr_value in snr:
    ber_iterations = []
    for it in range(iterations):
        tx_bits = np.random.randint(0, 2, N)
        tx_signal = 2 * tx_bits - 1
        linear_snr = 10 ** (snr_value / 10)
        noise_var = 1 / linear_snr
        noise = np.sqrt(noise_var) * np.random.randn(N)
        rx = tx_signal + noise
        rx_bits = []
        for i in range(N):
            if rx[i] >= 0:
                rx_bits.append(1)
            else:
                rx_bits.append(0)
        errors = 0
        for i in range(N):
            if tx_bits[i] != rx_bits[i]:
                errors += 1
        ber = errors / N
        ber_iterations.append(ber)
    average_ber = np.mean(ber_iterations)
    avg_ber.append(average_ber)
    print(f"SNR = {snr_value:2d} dB | Average BER = {average_ber:.6f}")

plt.figure(figsize=(8, 5))
plt.semilogy(snr, avg_ber, 'o-')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR using Monte Carlo Simulation")
plt.grid(True)

plt.show()