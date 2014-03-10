#!/usr/bin/env python

import matplotlib.pyplot as plt

# dict: {title of plot : [measure value files]}
# The input data may not have a \n at file end.

inputFiles = {'LibMergeSort_Sortierszenarien_im_Vergleich':
            ['sorted', 'shuffle', 'reverse']}

# different colors of the function graphs
COLORS = ['g', 'k', 'm']
print(inputFiles.items())
counter = 0

for outputFileName, fileNames in inputFiles.items():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    for fileName in fileNames:
        with open(fileName) as f:
            data = f.read()
        data = data.split('\n')
        #print(str(fileName) + str(data))
        x = [row.split()[0] for row in data]
        y = [float(row.split()[1]) for row in data]
        err = [float(row.split()[2]) for row in data]
        ax1.plot(x, y, c=COLORS[counter], label=fileName)
        ax1.errorbar(x, y, yerr=err, fmt='_',
                     ecolor=COLORS[counter], capthick=2)
        counter = counter + 1

    # ax1.set_title(outputFileName)
    ax1.set_xlabel('Anzahl Elemente N')
    ax1.set_ylabel('Laufzeit [s]')
    leg = ax1.legend(loc='upper left')
    #leg = ax1.legend(loc='lower right')
    # ax1.set_yscale('log')
    fig.savefig(outputFileName + '.pdf', format='pdf')
# plt.show()
