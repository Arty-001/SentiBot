import matplotlib.pyplot as plt
import numpy as np
import csv

def time_graph():
    x= range(1,101)
    y=[]

    with open('timeByTime.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            y.append(float(row[0]))
    plt.rcParams["font.size"] = 15  
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=[15.,8.])
    ax.margins(-.29,0.1)
    ax.plot(x,y, marker='o')
    ax.set_xlabel('Tweet time (sorted from latest to oldest)')
    ax.set_ylabel('Sentiment')
    ax.set_title("Sentiment analysis")
    plt.show()