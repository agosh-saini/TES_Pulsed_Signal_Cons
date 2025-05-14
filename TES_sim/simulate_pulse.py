"""
Author: Agosh Saini
Contact: contact@agoshsaini.com
================
Pulse generation 
""" 

import numpy as np
import matplotlib.pyplot as plt

__all__ = ['Pulse']  # Explicitly declare what should be exported

class Pulse:
    def __init__(self, amplitude, t_rise, t_fall, duration=1, dt=0.001):
        self.amplitude = amplitude
        self.t_rise = t_rise
        self.t_fall = t_fall
        self.duration = duration
        self.dt = dt
        self.t = np.arange(0, duration, dt)
        self.pulse = self._generate_pulse()

    def _generate_pulse(self):
        return self.amplitude * (1 - np.exp(-self.t / self.t_rise)) * np.exp(-(self.t - self.t_rise) / self.t_fall)
    
    def return_pulse(self):
        return self.pulse
    
    def return_parameters(self):
        return self.amplitude, self.t_rise, self.t_fall, self.duration, self.dt
    
    def plot(self):
        plt.plot(self.t, self.pulse)
        plt.show()


if __name__ == "__main__":
    pulse = Pulse(amplitude=1, t_rise=0.1, t_fall=0.1, duration=1, dt=0.01)
    pulse.plot()








