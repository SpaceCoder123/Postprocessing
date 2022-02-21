import matplotlib.pyplot as plt
from numpy import full
import pandas as pd

# Code devoloped by Dr. Gopalakrishna N


# Requirements 
# Python 3.5 or greater
# numpy 1.22.1
# pandas 1.3.5
# matplotlib 3.5.1

# param - parameter to plot

# tutorial case
# excel is provided for example plotting

col_list = ['SPL','TIME'] # headings given in excel (Case sensitive)
full_data= pd.read_excel("DATA.xlsx") #read the excel, make sure the excel is in the same repository

#line 24-25 removes all unwated blank spaces in the data collected

#param1_Xdata=(full_data[(col_list[0])].dropna()) 
#param1_Ydata=(full_data[(col_list[1])].dropna())


fig, ax = plt.subplots()

ax.tick_params(axis='both', which='major', labelsize=15) #sets subplots for all data,
# LABELSIZE: change font size in label size 
# TICK PARAMS: Change the appearance of ticks, tick labels, and gridlines a parameter defined in WHICH

plt.semilogx(full_data[0],full_data[2])

#plt.plot(param2_Xdata,param2_Ydata)

#plt.plot(param3_Xdata,param3_Ydata)

plt.legend(["Probe1"]) #legend

plt.show()

#main features of this code
# can plot data which have varying grid points (Grid Independent Data) in the same plot
