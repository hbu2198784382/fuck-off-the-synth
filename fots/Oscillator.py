import numpy as np

class Oscillator:
    def __init__(self, wave, sample_rate:int = 44100):
        """Initialize an Oscillator object

        Args:
            wave (function): The waveform function to be used.With period of 2pi.
            sample_rate (int, optional): The sample rate of the audio signal. Defaults to 44100.
        """
        self.wave = wave
        self.sr = sample_rate

    def generate(self, stime:float, freq:float, amp:float,phase:int = 0):
        """Generate a waveform using the given waveform function and parameters

        Args:
            stime (float): The sustain time of the waveform.
            freq (float): The frequency of the waveform.
            amp (float): The amplitude of the waveform.
            phase (int, optional): The initial phase of the waveform. Defaults to 0.

        Returns:
            _type_: _description_
        """
        tn = np.linspace(0, stime, self.sr*stime)
        return amp*self.wave(2*np.pi*freq*tn + phase)
        