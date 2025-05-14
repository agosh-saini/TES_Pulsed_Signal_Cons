"""
Author: Agosh Saini
Contact: contact@agoshsaini.com
================
Extract energy from a TES signal.
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

__all__ = ['EnergyExtractor'] 

class EnergyExtractor:
    def __init__(self, signal, dt=0.001):
        self.signal = signal
        self.dt = dt
        self.energy = self._calculate_energy()

    def _calculate_energy(self):
        return integrate.simpson(self.signal, dx=self.dt)

    def plot_signal(self):
        plt.plot(self.signal)
        plt.show()
        

if __name__ == "__main__":
    signal = np.random.randn(1000)
    energy_extractor = EnergyExtractor(signal)
    energy_extractor.plot_signal()
    print(energy_extractor.energy)


