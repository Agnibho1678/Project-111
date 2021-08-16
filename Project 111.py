import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("newdata.csv") 
data = df["average"].tolist()

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,30)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean
    
mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)
    
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(data)
mean_sample = statistics.mean(mean_list)

print("Mean is ", mean)
print("Standard Deviation is ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)

fig = ff.create_distplot([data],["Maths Scores"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y = [0,0.20], mode = "lines", name="MEAN"))
fig.show()

z_score = (mean - mean_sample)/std_deviation
print ("Z-score is ", z_score)