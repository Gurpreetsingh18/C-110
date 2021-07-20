import pandas as pd 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
population_mean= statistics.mean(data)
population_sd= statistics.stdev(data)

print("p mean and sd",population_mean,population_sd)

def cal_mean(counter):
    sample_data = []
    for i in range(0,counter):
        r = random.randint(0,len(data)-1)
        d = data[r]
        sample_data.append(d)
    mean = statistics.mean(sample_data)
    return mean

mean_list=[]
for j in range(0,100):
    m = cal_mean(1000)
    mean_list.append(m)

sample_mean= statistics.mean(mean_list)
sample_sd= statistics.stdev(mean_list)

print("s mean and sd",sample_mean,sample_sd)

fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 12], mode="lines", name="MEAN"))
fig.show()