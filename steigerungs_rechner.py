import csv
import matplotlib.pyplot as plt
import numpy as np

def stockAV(path, ave, low, high):

    if path == '':
        path = 'stock.csv'

    #get Data
    f = open(path, newline='')
    #convert data
    stock_csv = csv.DictReader(f, delimiter=',')

    #INT in Array name mean Float

    #def arrays for highes
    stock_array_High= []
    stock_array_Date= []
    stock_array_High_INT= []

    #def array for ableitung
    stock_array_ab =[]

    #def array for lowest
    stock_array_Low= []

    stock_array_Low_INT= []

    #def array for Close
    stock_array_Close = []
    stock_array_Close_INT = []

    intItem = 1
    item2 = "string string 2"
    #data in arrays
    for item in stock_csv:
        #print(item)

        print(item['High'])
        stock_array_High.append(item['High'])

        stock_array_Low.append(item['Low'])
        stock_array_Date.append((item['Date']))

        stock_array_Close.append(item['Close'])

        #low
        item3 = str(item['Low'])
        floatItemLow = float(item3)
        stock_array_Low_INT.append(floatItemLow)

        #high
        item2 = str(item['High'])
        #item2.replace(".", ",")
        floatItem = float(item2)
        stock_array_High_INT.append(floatItem)

        #close
        item3 = str(item['Close'])
        floatItemClose = float(item3)
        stock_array_Close_INT.append(floatItemClose)

        #ableitung
        item4 = str(item['High'])
        floatItemAb = float(item4)
        stock_array_ab.append(floatItemAb)





    print("NEW ")
    #data in array
    for item in stock_array_High:

        print(item)

    #data into diagram
    xpoints = np.array(stock_array_Date)
    ypoints = np.array(stock_array_High_INT)

    ypointsLow = np.array(stock_array_Low_INT)

    ypointsClose = np.array(stock_array_Close_INT)

    #average
    ave_Array =[]
    sub_ave_Array = []
    x1 = 8
    for x1 in range(len(stock_array_High_INT)):
        for y in range(7):
            sub_ave_Array.append(stock_array_High_INT[x1-y])
        print("SUB:" + str(sub_ave_Array))
        ave_Array.append(np.mean(sub_ave_Array))
        sub_ave_Array.clear()

    #ableitung
    stock_array_ableitung = []
    x2 = 1

    for x2 in range(len(stock_array_High_INT)-1):
        stock_array_ableitung.append((stock_array_High_INT[x2]/stock_array_High_INT[x2-1])/(x2-(x2-1)))
        print("ableitung")
        print (stock_array_ableitung[x2])

    stock_array_ableitung2 = np.poly1d(stock_array_High_INT)
    derivative = stock_array_ableitung2.deriv()
    print("ABLEITUNG")
   # print(derivative)



    #pitch
    yP_first = stock_array_High_INT[0]
    print(len(stock_array_High_INT))
    yP_last = stock_array_High_INT[len(stock_array_High_INT)-1]

    #pitch 1Y
    yP_first_1Y = stock_array_High_INT[len(stock_array_High_INT)-250]
    yP_last_1Y = stock_array_High_INT[len(stock_array_High_INT) - 1]


    #lowest highest positon
    max_N = max(stock_array_High_INT)
    min_N = min(stock_array_High_INT)


    #name the diagram
    lableName = "DQ: " + str(round(yP_last-yP_first, 2)) + " / ave DQ: " + str(round(((yP_last-yP_first)/ len(stock_array_High_INT)), 2))

    plt.figure(figsize=(5, 2.7), layout='constrained')

    #plot ave
    if ave:
        plt.plot(ave_Array, color = "blue", linewidth = 2, linestyle = 'dotted', label = "average over 20 days")

    #plot ableitung
    plt.plot(stock_array_ableitung, color = "red", linewidth = 2, linestyle = 'dotted', label = "Ableitung")

    #plot lowerst and highest
    plt.plot([1, len(stock_array_High_INT)-1], [min_N, min_N], color="red", linewidth=3, linestyle="--", label = "MIN")
    plt.plot([1, len(stock_array_High_INT)-1], [max_N, max_N], color="green", linewidth=3, linestyle="--", label = "MAX")
    print("MIN"+ str(min_N))

    #plot pitch 1Y
    plt.plot([len(stock_array_High_INT)-250, len(stock_array_High_INT)-1], [yP_first_1Y, yP_last_1Y], label = '1Y pitch')

    #plot pitch
    plt.plot([1, len(stock_array_High_INT)-1], [yP_first, yP_last], label = lableName)

    #plot aktie highes
    if high:
        plt.plot(ypoints, alpha=0.8)

    #plot aktie lowest
    if low:
     plt.plot(ypointsLow, label = 'lowestPoints', color = "#5900d1", alpha=0.8)

    #plot normal chart / Close
    plt.plot(ypointsClose, label = 'Close-Chart', color = 'black', alpha=1)





    plt.xlabel('Day')
    plt.ylabel('Aktie')
    plt.legend(title="Line names",loc='upper left')
    plt.show()

