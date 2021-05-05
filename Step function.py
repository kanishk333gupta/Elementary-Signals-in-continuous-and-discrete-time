#STEP FUNCTION

from numpy import*			                        #Importing all definitions from the module numpy
import matplotlib.pyplot as mplot			        #Shortening as mplot ,an alias to call the library name

###CONTINUOUS

#Defining Step function of time , amplitude and shift
# Using for loop in the range
# Checking if condition
# putting new value
# Ends execution and returns the step function
def step_func_CT(t1,A,shift):
    for i in range(0,N):
        if t1[i]>=-shift:
            uCT[i]=A
    return uCT
t1=linspace(-100,100,10000) 			           	# 10000 linearly spaced numbers from -100 to 100
N=len(t1)                                      	   	# Finds the length of array
uCT=zeros(N)                                    	#Zeros gives a new array of given numbers filled as zeros
uCT=step_func_CT(t1,1,0)  		                    # Calling step function
mplot.plot(t1,uCT)		                            #Plot a unit step signal
mplot.xlim(-10, 10)						            # Sets the limits of  X-axis in plot
mplot.ylim(-3, 3)				            		# Sets the limits of  Y-axis in plot
mplot.gca().spines['left'].set_position('center')	# Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center') # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')		# Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')			# Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')		# Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')			# Make colors invisible of corner lines
x_position=list(range(-10, 10))				        # Fixing the X-axis from -10 to 10
y_position=list(range(-3, 3))					    # Fixing the Y-axis form -3 to 3
#Ticks are the markers denoting data points on axes
mplot.xticks([i+1 for i in x_position])			    # Sets and iterates X-axis tick values
mplot.yticks([i+1 for i in y_position])			    # Sets and iterates Y-axis tick values
mplot.title('Step function in Continuous time') 	# Give a title for the step signal plot
mplot.grid()							            # Showing grid
mplot.show()				            			# Display the step signal

###DISCRETE

# Defining step function with amplitude and shift
#Initializing value to zeros
# Using for loop for the given range
# Checking for condition using if
# Giving value to variable
#Ends execution and returns step signal
def step_fun_DT(n, A, shift):
    uDT = zeros(N)
    for i in range (0, N):
        if n[i]>=-shift:
            uDT[i] = A
    return uDT
n=arange(-10, 10)	                                #Returns an array with evenly spaced elements as per the interval forX-axis(start,stop)
N=len(n) 							                # Returns the number of items in an object
A=1								                    # Setting Amplitude as 1 for initial
mplot.rcParams['figure.figsize']=(8, 5)  			# Fixing the figure size
uDT=step_fun_DT(n, 1, 0) 	                        #Calling the step function with n as a variable,magnitude as1 and shift=0
mplot.stem(n,uDT,use_line_collection=True)	        # plot the stem plot for step function ( use_line_collection Improves the performance of stem plot)
mplot.xlim(-10, 10)						            # Sets the limits of  X-axis in plot
mplot.ylim(-3, 3)						            # Sets the limits of  Y-axis in plot
mplot.gca().spines['left'].set_position('center')	# Setting the axes at the centre
mplot.gca().spines['bottom'].set_position('center') # Setting the axes at the centre
mplot.gca().spines['bottom'].set_color('red')		# Setting the X-axis color as red
mplot.gca().spines['left'].set_color('red')			# Setting the Y-axis color as red
mplot.gca().spines['right'].set_color('none')		# Make colors invisible of corner lines
mplot.gca().spines['top'].set_color('none')			# Make colors invisible of corner lines
x_position=list(range(-10, 10))				        # Fixing the X-axis in range -10 to 10
y_position=list(range(-3, 3))					    # Fixing the Y-axis in range -3 to 3
#Ticks are the markers denoting data points on axes
mplot.xticks([i+1 for i in x_position])			    # Sets and iterates X-axis tick values
mplot.yticks([i+1 for i in y_position])			    # Sets and iterates Y-axis tick values
mplot.title('Step function in Discrete time')		# Give a title for the step signal plot
mplot.grid()							            # Showing grid
mplot.show()							            # Display the step signal
