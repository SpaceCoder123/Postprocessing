import matplotlib.pyplot as plt

# make sure there are no empty spaces in the dat file
datContent = [i.strip().split() for i in open("random_Data.dat").readlines()]
# every line is read as a string in the file and will be added in to the array of datcontent

xdata = []
ydata = []
n = len(datContent)
for x in range(0,n):
    # conversion of data from string to float and appending it to main array
    xdata.append(float(datContent[x][0].upper().replace(',','')))
    ydata.append(float(datContent[x][1].upper().replace(',','')))


#follow the same format
plt.figure("Semilog Plot")
plt.xlabel('X-axis name')
plt.ylabel('Y-axis name')
plt.semilogx(xdata,ydata)
plt.legend(['Legend_name'])
plt.show()
