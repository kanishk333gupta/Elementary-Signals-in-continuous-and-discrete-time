#RAMP SIGNAL

from numpy import*			                        #Importing all definitions from the module numpy
import matplotlib.pyplot as mplot			        #Shortening as mplot ,an alias to call the library name


###CONTINUOUS TIME

#defining Ramp function
#Initializing ramp variable as an empty list
#Applying for loop
#And checking for condition if input is less than 0 ,then return 0
#else append it into the given list
#End the execution and return ramp
def ramp_fn(n):
    ramp = []
    for list in n:
        if list < 0:
            ramp.append(0)
        else:
            ramp.append(list)
    return ramp
UP = 10                                             # Setting upper limit as 10
LP = -10                                            # Setting lower limit as 10
n = arange(LP, UP, 1)                               # Returns an array with evenly spaced elements as per the interval(start,stop,step )
r = ramp_fn(n)                                      # Calling Ramp function
mplot.plot(n, r)                                    # Plot a Ramp signal
mplot.title('Ramp Function in Continuous r[t]')     # Give a title for the Ramp signal plot
mplot.xlim(-10, 10)                                 # Sets the limits of  X-axis in plot
mplot.ylim(-10, 10)                                 # Sets the limits of Y-axis in plot
mplot.gca().spines['left'].set_position('center')   # Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center') # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')       # Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')         # Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')       # Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')         # Make colors invisible of corner lines
# Ticks are the markers denoting data points on axes
mplot.xticks(arange(LP, UP, 1))                     # Sets the X-axis tick values in given interval
mplot.yticks(arange(LP, UP, 1))                     # Sets the Y-axis tick values in given interval
mplot.grid()                                        # Showing grid
mplot.show()                                        # Display the ramp signal in continuous time

###DISCRETE TIME

mplot.stem(n, r)                                    # plot the stem plot for ramp function
mplot.title('Ramp Function in Discrete TIme r[n]')  # Give a title for the ramp signal plot
mplot.xlim(-10, 10)                                 # Sets the limits of  X-axis in plot
mplot.ylim(-10, 10)                                 # Sets the limits of  Y-axis in plot
mplot.gca().spines['left'].set_position('center')   # Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center') # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')       # Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')         # Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')       # Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')         # Make colors invisible of corner lines
# Ticks are the markers denoting data points on axes
mplot.xticks(arange(LP, UP, 1))                     # Sets the X-axis tick values in the given interval
mplot.yticks(arange(LP, UP, 1))                     # Sets the Y-axis tick values in the given interval
mplot.grid()                                        # Showing grid
mplot.show()                                        # Display the ramp signal in discrete time


####THANK YOU