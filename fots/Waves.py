import numpy as np

class Waves:
    def sinwave(x):
        """
        Returns the sine wave of x.With period 2*pi.

        Args:
            x (float or numpy array): The input value(s).

        Returns:
            float or numpy array: The sine wave of x.
        """
        return np.sin(x)

    def squarewave(x):
        """
        Returns the square wave of x.With period 2*pi.

        Args:
            x (float or numpy array): The input value(s).

        Returns:
            float or numpy array: The square wave of x.
        """
        return np.sign(np.sin(x))

    def sawtoothwave(x):
        """
        Returns the sawtooth wave of x.With period pi.

        Args:
            x (float or numpy array): The input value(s).

        Returns:
            float or numpy array: The sawtooth wave of x.
        """
        return 2*(np.mod(x,2)-1)

    def trianglewave(x):
        """
        Returns the triangle wave of x.With period pi.

        Args:
            x (float or numpy array): The input value(s).

        Returns:
            float or numpy array: The triangle wave of x.
        """
        return 2*np.abs(np.mod(x,2)-1)-1
