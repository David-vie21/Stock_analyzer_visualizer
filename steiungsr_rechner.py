import csv
import matplotlib.pyplot as plt
import numpy as np
#get Data
f = open('TSLA.csv', newline='')
#convert data
tsla_csv = csv.DictReader(f, delimiter=',')
#def arrays
tsla_array_High= []
tsla_array_Date= []
tsla_array_High_INT= []

intItem = 1
item2 = "string string 2"
#data in arrays
for item in tsla_csv:
    #print(item)

    print(item['High'])
    tsla_array_High.append(item['High'])
    tsla_array_Date.append((item['Date']))
    item2 = str(item['High'])
    #item2.replace(".", ",")
    floatItem = float(item2)
    tsla_array_High_INT.append(floatItem)



print("NEW ")
#data in array
for item in tsla_array_High:

    print(item)

#data into diagram
xpoints = np.array(tsla_array_Date)
ypoints = np.array(tsla_array_High_INT)

#pitch
yP_first = tsla_array_High_INT[0]
print(len(tsla_array_High_INT))
yP_last = tsla_array_High_INT[len(tsla_array_High_INT)-1]

#lowest highest positon
max_N = max(tsla_array_High_INT)
min_N = min(tsla_array_High_INT)


#name the diagram
lableName = "DQ: " + str(round(yP_last-yP_first, 2))

plt.figure(figsize=(5, 2.7), layout='constrained')


#plot lowerst and highest
plt.plot([1, len(tsla_array_High_INT)-1], [min_N, min_N], color="red", linewidth=3, linestyle="--", label = "MIN")
plt.plot([1, len(tsla_array_High_INT)-1], [max_N, max_N], color="green", linewidth=3, linestyle="--", label = "MAX")
print("MIN"+ str(min_N))


#plot pitch
plt.plot([1, len(tsla_array_High_INT)-1], [yP_first, yP_last], label = lableName)
#plot aktie
plt.plot(ypoints)






plt.xlabel('Day')
plt.ylabel('Aktie')
plt.legend(title="Line names",loc='upper left')
plt.show()