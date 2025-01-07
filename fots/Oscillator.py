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

    def generate(self, duration:float, freq:float, amp:float,phase:int = 0) -> np.ndarray:
        """Generate a waveform using the given waveform function and parameters

        Args:
            duration (float): The sustain time of the waveform.
            freq (float): The frequency of the waveform.
            amp (float): The amplitude of the waveform.
            phase (int, optional): The initial phase of the waveform. Defaults to 0.

        Returns:
            np.ndarray: The generated waveform.
        """
        tn = np.linspace(0, duration, self.sr*duration)
        return amp*self.wave(2*np.pi*freq*tn + phase).astype(np.float32)
        