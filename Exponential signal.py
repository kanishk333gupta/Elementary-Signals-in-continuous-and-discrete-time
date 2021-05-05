#EXPONENTIAL SIGNAL

import numpy as np                  #Importing all definitions from the module and shortening as np
import matplotlib.pyplot as mplot   #Shortening as mplot ,an alias to call the library name

###CONTINUOUS

x = np.linspace(-1, 2, 100)         # 100 linearly spaced numbers from -1 to 2
xCT = np.exp(x)						# Exponent function
mplot.plot(x , xCT)	                # Plot a exponential signal
mplot.xlabel('x') 					# Give X-axis label for the Exponential signal plot
mplot.ylabel('exp(x)')				# Give Y-axis label for the Exponential signal plot
mplot.title('Exponential Signal in Continuous Time')#Give a title for the Exponential signal plot
mplot.grid()						# Showing grid
mplot.show()						# Display the Exponential signal

###DISCRETE

#Defining a function to generate DISCRETE Exponential signal
# Initializing exponential variable as an empty list
# Using  for loop in range
# and entering new values in the list
# Ends execution and return the exponential value
def exp_DT(a, n):
    exp = []
    for range in n:
        exp.append(np.exp(a*range))
    return exp
a = 2                               # Input the value  of constant
n = np.arange(-1, 1, 0.1)           #Returns an array with evenly spaced elements as per the interval(start,stop,step )
x = exp_DT(a, n)					# Calling Exponential function
mplot.stem(n, x)					# Plot the stem plot for exponential wave
mplot.xlabel('n') 					# Give X-axis label for the Exponential signal plot
mplot.ylabel('x[n]')				# Give Y-axis label for the Exponential signal plot
mplot.title('Exponential Signal in Discrete Time')	# Give a title for the exponential signal plot
mplot.grid()						# Showing grid
mplot.show()						# Display the exponential signal
