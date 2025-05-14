"""
Author: Agosh Saini
Contact: contact@agoshsaini.com
================
Add noise to a TES signal.
""" 

import numpy as np
import matplotlib.pyplot as plt

__all__ = ['Noise']  # Explicitly declare what should be exported

class Noise:
    def __init__(self, signal, mean=0, std_dev=0.1):
        self.signal = signal
        self.mean = mean
        self.std_dev = std_dev
        self.noise = self._generate_noise()
        self.noisy_signal = self.signal + self.noise

    def _generate_noise(self):
        return np.random.normal(self.mean, self.std_dev, len(self.signal))

    def plot_noise(self):
        plt.plot(self.noise)
        plt.show()

    def plot_noisy_signal(self):
        plt.plot(self.noisy_signal)
        plt.show()


if __name__ == "__main__":
    signal = 100*(1-np.exp(-np.linspace(0, 1, 1000)))
    noise = Noise(signal, mean=0, std_dev=0.1)
    noise.plot_noise()
    noise.plot_noisy_signal()


