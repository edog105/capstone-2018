# To use this code, please change the user inputs as needed and run "python3 plot_data.py"
# on the command line. The program reads data from a .txt file and generates a .png figure 
# file of the temperature (degrees Celsius) against time (seconds) graph.

# IMPORTS #
import numpy as np
import matplotlib.pyplot as plt
###########

# USER INPUTS #
filename = "2018-10-18/2018-10-18_1444.txt"  # Enter input filename.
plotname = "2018-10-18/2018-10-18_1444.png"  # Enter output figure file name.
###############

# Load data from input text file.
data = np.loadtxt(filename, delimiter=', ')
time = data[:, 0]
a0_temp = data[:, 1]
a1_temp = data[:, 2]
a2_temp = data[:, 3]

# Plot loaded data.
plt.figure()
plt.plot(time, a0_temp, label='Air Control')
plt.plot(time, a1_temp, label='Styrofoam Control')
plt.plot(time, a2_temp, label='PDMS')
plt.grid()
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (degrees Celsius)')
plt.savefig(plotname)
