# Weekly Task 8
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10], 
# on the one set of axes.
# Some marks will be given for making the plot look nice (legend etc).
# Author: Ciaran Moran
import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation
mean = 5
standardDeviation = 2

# Set the 1000 random values using the above
rnd = np.random.normal(mean, standardDeviation, 1000)

# Set the histogram
plt.hist(rnd, bins=20, density=True) 

# This based on code I found via Google on
# https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
# adjusting that example from x ** 2
# Also used this for changing the colour to cyan
#https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/
x = np.linspace(0, 10, 100)
y = x ** 3
plt.plot(x, y,color = 'cyan')

# Finally set and show the plot
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Histogram of normal distribution,plotting function h(x)=x3 in the range [0, 10]')
plt.show()