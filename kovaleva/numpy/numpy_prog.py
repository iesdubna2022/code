import numpy as np

def func(x):
    return np.exp(-(x ** 2)) * (np.sin(x) ** 2) * np.sin(x ** 2) 

def integrirov(func, first, last):
    
    step = (last - first) / 1000000
    
    x = np.arange(first, last, step)
    x = np.array(func(x))
    y = np.array(step * x)
    
    return y.sum()

rezult = integrirov(func, 0, 3)
print(round(rezult, 6))