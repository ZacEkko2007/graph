import matplotlib.pyplot as plt

month = ['mar', 'apr', 'may', 'jun', 'jul']
sales = [1, 5, 4, 8, 11]

# line graph
plt.figure(dpi=150) # dpi=x, figsize=(x,y) screen size control
plt.rc('font', family='Nanum Gothic')
plt.title("Monthly Sale Quantity")
plt.plot(month, sales, color = "aqua", label = "SongMJ")
plt.legend(loc = "upper right") 
# plt.legend(): label option add    loc = "upper(or lower, center) left(or right, center)": position to appear
plt.xlabel('month')
plt.ylabel("sales")
plt.show()

# bar graph
plt.figure(dpi=150)
plt.rc('font', family='Malgun Gothic')
plt.title("Monthly Sale Quantity")
plt.bar(month, sales, color = "aqua", label = 'SongMJ', edgecolor = 'black') 
# barh(): change bar direction, x and y was swapped
plt.legend(loc = 'upper right')
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

# histogram
import numpy as np

data = np.random.randn(1000)

plt.figure(dpi=150)
plt.hist(data ,color = 'aqua' ,edgecolor = 'black', histtype = 'bar', label = 'data', bins = 50) 
# histtype = 'bar(or barstacked, step, stepfilled)'  bins = x: set section
plt.legend(loc = 'upper right')
plt.show()

# pie graph
bloodType = ['A-type', 'B-type', 'O-type', 'AB-type']
bloodCount = [34, 27, 38, 11]
plt.figure(dpi=150)
plt.rc('font', family = 'Malgun Gothic')
plt.title("Korean Blood Type Ratio")
plt.pie(bloodCount, labels = bloodType, autopct = '%1.1f%%') 
# autopct = '%1.xf%%': the x place percentage display       colors = []: set colors in order
plt.show()

# scatter graph 
# to be added soon
