#IMPULSE FUNCTION

from numpy import*			                        #Importing all definitions from the module numpy
import matplotlib.pyplot as mplot			        #Shortening as mplot ,an alias to call the library name

###CONTINUOUS TIME

def impulse(x):						                # Defining impulse function
	return where(abs(x)<=0.5, 1, 0) 			    # Ends execution , Return absolute value of function
x = linspace(-10,  10,  100)					    # Plots 100 linearly spaced numbers from -10 to 10
r = impulse(x)							            # Calling impulse function
mplot.plot(x, r)	 					            # Plot a impulse signal
mplot.xlabel('t')  					            	# Give X-axis label for the Impulse signal plot
mplot.ylabel('d[t]')						        # Give Y-axis label for the Impulse signal plot
mplot.title('Unit Impulse in Continuous time at D(0)')	# Give a title for the Impulse signal plot
mplot.grid()							            # Showing grid
mplot.show()							            # Display the impulse signal

###DISCRETE TIME

#Defining a impulse function
#Initializing impulse variable as an empty list
#Applying for loop and checking for condition
#if input is equal to i then append 1 , else append it to 0
#end the execution and return impulse
def unit_impulse_DT(i, n):
    impulse =[]
    for list in n:
        if list == i:
            impulse.append(1)
        else:
            impulse.append(0)
    return impulse
i = 0								                # setting i as 0
pstv_x = 7							                # Setting positive X-axis as 7
ngtv_x = -7							                # Setting negative X-axis as -7
n = arange(ngtv_x, pstv_x, 1)                       #Returns array with evenly spaced elements as per the interval(start,stop,step)
d = unit_impulse_DT(i, n)					        # Calling Impulse function
mplot.stem(n, d)						            # Plot the stem plot for impulse signal
mplot.xlabel('n') 						            # Give X-axis label for the Impulse signal plot
mplot.ylabel('d[n]') 						        # Give Y-axis label for the Impulse signal plot
mplot.title('Unit Impulse in Discrete time at D(0)')# Give a title for the impulse signal plot
mplot.grid()							            # Showing grid
mplot.show()							            # Display the impulse signal
