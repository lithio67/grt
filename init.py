import random
import numpy as np

# Alias for print()
say = print

# Alias for random.random()
def ran():
    return random.random()

# Alias for numpy.array()
def arr(*args, **kwargs):
    return np.array(*args, **kwargs)
