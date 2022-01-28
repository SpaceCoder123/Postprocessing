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

col_list = ["Location_3L","Pressure_3L","Location_6L","Pressure_6L","Location_12L","Pressure_12L"] # headings given in excel (Case sensitive)
full_data= pd.read_excel("pressure_data_grid.xlsx",usecols=col_list) #read the excel, make sure the excel is in the same repository

#line 8-15 removes all unwated blank spaces in the data collected

param1_Xdata=(full_data[(col_list[0])].dropna()) 
param1_Xdata=(full_data[(col_list[1])].dropna())
param2_Xdata=(full_data[(col_list[2])].dropna())
param2_Ydata=(full_data[(col_list[3])].dropna())
param3_Xdata=(full_data[(col_list[4])].dropna())
param3_Ydata=(full_data[(col_list[5])].dropna())

fig, ax = plt.subplots()
ax.tick_params(axis='both', which='major', labelsize=15) #sets subplots for all data,LABELSIZE changes font size in label size 

plt.plot(param1_Xdata,param1_Xdata)

plt.plot(param2_Xdata,param2_Ydata)

plt.plot(param3_Xdata,param3_Ydata)

plt.legend(["Param1","Param 2","Param 3"]) #legend

plt.show()

#main features of this code
# can plot data which have varying grid points (Grid Independent Data) in the same plot
