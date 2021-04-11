import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("medium_data.csv")
data=df['reading_time'].tolist()
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    std=statistics.stdev(dataset)
    print(mean)
    print(std)
    return mean

def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(meanlist)
    print(mean)
    std=statistics.stdev(meanlist)
    print(std)
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(500)
        meanlist.append(setofmeans)

    showfig(meanlist)
setup()