#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 01:38:00 2026

@author: santoshsoni
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1200
t = np.arange(0,T,1/fs_dpcm)
m= 2*np.sin(2*np.pi*30*t)+ 4*np.cos(2*np.pi*60*t)
