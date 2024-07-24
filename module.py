# module.py

import random
from array import array

def say(message):
    """
    Alias for print().
    
    Parameters:
    message (str): The message to print.
    """
    print(message)

def ran():
    """
    Alias for random.random().
    
    Returns:
    float: A random float number between 0.0 and 1.0.
    """
    return random.random()

def arr(typecode, initializer):
    """
    Alias for array.array().
    
    Parameters:
    typecode (str): The type code of the array.
    initializer (iterable): An iterable with initial values for the array.
    
    Returns:
    array.array: An array object.
    """
    return array(typecode, initializer)

if __name__ == "__main__":
    # Test the functions
    say("Hello, World!")
    print(ran())
    print(arr('i', [1, 2, 3, 4]))
