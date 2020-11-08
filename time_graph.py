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
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.plot(x,y, marker='o')
    ax.set_xlabel('Tweet time')
    ax.set_ylabel('Sentiment')
    ax.set_title("Sentiment analysis")
    plt.show()