"""
Author: Agosh Saini
Contact: contact@agoshsaini.com
================
Signal filtering and processing algorithms.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.optimize import curve_fit
__all__ = ['Filter']

class Filter:
    def __init__(self, input_signal, f_cutoff=100, sample_rate=1000):
        self.input_signal = input_signal
        self.f_cutoff = f_cutoff
        self.sample_rate = sample_rate
        self.signal_filtered = self.low_pass() 


    def low_pass(self):
        nyquist = 0.5 * self.sample_rate
        cutoff = self.f_cutoff / nyquist
        b, a = butter(N=4, Wn=cutoff, btype='low')
        return filtfilt(b, a, self.input_signal)
    

    def plot_filter(self):
        plt.figure(figsize=(10, 4))
        plt.plot(self.input_signal, label="Original", alpha=0.5)
        plt.plot(self.signal_filtered, label="Filtered", linewidth=2)
        plt.legend()
        plt.title("Low-pass Filtered Signal")
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    t = np.linspace(0, 1, 1000)
    # Simulate low-frequency + high-frequency + noise
    input_signal = 1 * (1 - np.exp(-t / 0.1)) * np.exp(-(t - 0.1) / 0.2) + 0.1*np.random.normal(0, 1, len(t))   

    filt = Filter(input_signal=input_signal, f_cutoff=100, sample_rate=1000)
    filt.plot_filter()
