import numpy as np

# def function(x):
#     return np.sin(x) + np.cos(x) + 1
#
# def firstDefiv(x, function = function):
#     return np.cos(x) - np.sin(x)
#
# def secondDefiv(x, function = function):
#     return -np.sin(x) - np.cos(x)
#
# def thirdDefiv(x, function = function):
#     return -np.cos(x) + np.sin(x)

def function(x):
    return np.sin(x) + 0.5

def firstDefiv(x, function = function):
    return np.cos(x)

def secondDefiv(x, function = function):
    return -np.sin(x)

def thirdDefiv(x, function = function):
    return -np.cos(x)

# def function(x):
#     return x**5 + np.e**(-x) + 2*np.sin(x) + x
#
# def firstDefiv(x, function = function):
#     return 5*x**4 - np.e**(-x) + 2*np.cos(x) + 1
#
# def secondDefiv(x, function = function):
#     return 20*x**3 + np.e**(-x) - 2*np.sin(x)
#
# def thirdDefiv(x, function = function):
#     return 60*x**2 - np.e**(-x) - 2*np.cos(x)

# def function(x):
#     return x**2 + np.e**(-x) + 2*np.sin(x) + x
#
# def firstDefiv(x, function = function):
#     return 2*x - np.e**(-x) + 2*np.cos(x) + 1
#
# def secondDefiv(x, function = function):
#     return 2 + np.e**(-x) - 2*np.sin(x)
#
# def thirdDefiv(x, function = function):
#     return - np.e**(-x) - 2*np.cos(x)

