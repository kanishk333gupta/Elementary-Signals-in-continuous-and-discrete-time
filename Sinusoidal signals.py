#SINUSOIDAL SIGNAL

import numpy as np                  #Importing all definitions from the module and shortening as np
import matplotlib.pyplot as mplot   #Shortening as mplot ,an alias to call the library name

###CONTINUOUS

t1 = np.linspace(-10, 10, 100)      # 100 linearly spaced numbers from -10 to 10
A = 2                               # Amplitude of the sine wave
f0 = 30                             # Frequency of the sine wave
x = A * np.sin(2 * np.pi * f0 * t1) # Compute the value (amplitude) of the sine wave for each sample
mplot.plot(t1, x, '-b')             # Plot a sine wave using time and amplitude obtained for the sine wave
mplot.title(r'Continuous-time sinusoidal')  # Give a title for the sine wave plot
mplot.xlabel(r't (in s)')           # Give X-axis label for the sine wave plot
mplot.xlim(-10, 10)                 # Sets the limits of  X-axis in plot
mplot.ylim(-3, 3)                   # Sets the limits of  Y-axis in plot
mplot.gca().spines['left'].set_position('center')    # Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center')  # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')        # Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')          # Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')        # Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')          # Make colors invisible of corner lines
x_position = list(range(-10, 10))                    # Fixing the X-axis from -10 to 10
y_position = list(range(-3, 3))                      # Fixing the Y-axis from -3 to 3
# Ticks are the markers denoting data points on axes
mplot.xticks([i + 1 for i in x_position])            # Sets and iterates X-axis tick values
mplot.yticks([i + 1 for i in y_position])            # Sets and iterates Y-axis tick values
mplot.grid()                                         # Showing grid
mplot.show()                                         # Display the sine wave

###DISCRETE

A = 2                               # Amplitude of the sine wave
F0 = 0.05                           # Frequency of the sine wave
L = 100                             # Sample size
t2 = np.linspace(-50, 50, 100)      # 100 linearly spaced numbers from -50 to 50
n = np.arange(L)                    # Returns an array with evenly spaced elements
y = -A * np.sin(2 * np.pi * F0 * n) # Compute the value (amplitude) of the sin wave at the for each sample
mplot.stem(t2, y, '-b',use_line_collection=True)  # Plot the stem plot for sine wave
mplot.title('Discrete-time sinusoidal')  # Give a title for the sine wave plot
mplot.xlabel('n')                   # Give X-axis label for the sine wave plot
mplot.xlim(-50, 50)                 # Sets the limits of  X-axis in plot
mplot.ylim(-3, 3)                   # Sets the limits of  Y-axis in plot
mplot.gca().spines['left'].set_position('center')    # Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center')  # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')        # Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')          # Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')        # Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')          # Make colors invisible of corner lines
x_position = list(range(-10, 10))                    # Fixing the X-axis
y_position = list(range(-3, 3))                      # Fixing the Y-axis
# Ticks are the markers denoting data points on axes
mplot.xticks([4 * i + 1 for i in x_position])        # Sets and iterates X-axis tick values
mplot.yticks([i + 1 for i in y_position])            # Sets and iterates Y-axis tick values
mplot.grid()                                         # Showing grid
mplot.show()                                         # Display the sine wave
