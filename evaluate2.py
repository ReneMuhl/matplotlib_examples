#!/usr/bin/env python

import matplotlib.pyplot as plt

# dict: {title of plot : [measure value files]}
# The input data may not have a \n at file end.

inputFiles = {'AbweichungenZoom': ['1_1PE', '2_1PE']}

# different colors of the function graphs
COLORS = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
print(inputFiles.items())
counter = 0

for outputFileName, fileNames in inputFiles.items():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    for fileName in fileNames:
        with open(fileName) as f:
            data = f.read()
        data = data.split('\n')
        x = [row.split()[0] for row in data]
        y = [row.split()[1] for row in data]
        ax1.set_yscale("log")
        if(counter == 0):
            ax1.plot(x, y, c=COLORS[counter], label='Testfkt1')
        else:
            ax1.plot(x, y, c=COLORS[counter], label='Testfkt2')
        #ax1.set_xlim(0e-10, 0e-15)
        plt.ylim(0.0E-10, 0.0E-20)
        plt.xlim(-10, 1000)
        counter = counter + 1
        print(outputFileName + " " + fileName)

    # ax1.set_title(outputFileName)
    ax1.set_xlabel('Anzahl Partitonen n')
    ax1.set_ylabel('Abweichungen')
    leg = ax1.legend(loc='upper right')
    #leg = ax1.legend(loc='upper left')
    #leg = ax1.legend(loc='lower left')
    fig.savefig(outputFileName + '.pdf', format='pdf')
# plt.show()
