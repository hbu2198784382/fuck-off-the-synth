import numpy as np

class Sequence:
    def __init__(self,sample_rate=44100):
        self.sr = sample_rate
        self.sequence = np.array([]).astype(np.float32)

    def add(self, wave):
        self.sequence = np.append(self.sequence, wave)

    def get(self):
        return self.sequence
    
    def sleep(self, duration):
        self.sequence = np.append(self.sequence, self.sr*duration)