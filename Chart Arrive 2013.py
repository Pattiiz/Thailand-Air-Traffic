"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('Pattiiz', 'ph2g5dyom6')

def fetch_arrive_2013():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2013":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2013.append(temporary)
    return static_2013

def summary_arrive_2013():
    arrive_2013 = fetch_arrive_2013()
    summary_2013 = {}
    for run in arrive_2013:
        if run[0] in summary_2013:
            summary_2013[run[0]] += int(run[1])
        else:
            summary_2013[run[0]] = int(run[1])
    return summary_2013

def month_list():
    arrive_2013 = fetch_arrive_2013()
    month = []
    for run in range(0, 13):
        month.append(arrive_2013[run][0])
    return month

summary_2013 = summary_arrive_2013()
month = month_list()
trace0 = go.Bar(
    x=[run for run in month],
    y=[summary_2013[run] for run in month],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)
data = [trace0]
layout = go.Layout(
    title='Chart Arrive per Month 2013',
)
fig = go.Figure(data=data, layout=layout)
tls.embed(py.plot(fig, filename='Chart Arrive per Month 2013'))
