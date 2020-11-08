import matplotlib.pyplot as plt
import csv

def time_graph():
    x= range(1,101)
    y=[]

    with open('timeByTime.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            y.append(float(row[0]))


    plt.plot(x,y, marker='o')

    plt.title('Time-by-time analysis')

    plt.xlabel('Time commenting')
    plt.ylabel('Sentiment')

    plt.show()

