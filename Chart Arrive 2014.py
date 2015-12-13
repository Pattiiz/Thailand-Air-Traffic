"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('Pattiiz', 'ph2g5dyom6')

def fetch_arrive_2014():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2014":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2014.append(temporary)
    return static_2014

def summary_arrive_2014():
    arrive_2014 = fetch_arrive_2014()
    summary_2014 = {}
    for run in arrive_2014:
        if run[0] in summary_2014:
            summary_2014[run[0]] += run[1]
        else:
            summary_2014[run[0]] = run[1]
    return summary_2014

def month_list():
    arrive_2014 = fetch_arrive_2014()
    month = []
    for run in range(0, 13):
        month.append(arrive_2014[run][0])
    return month

summary_2014 = summary_arrive_2014()
month = month_list()
trace0 = go.Bar(
    x=[run for run in month],
    y=[summary_2014[run] for run in month],
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
    title='Chart Arrive per Month 2014',
)
fig = go.Figure(data=data, layout=layout)
tls.embed(py.plot(fig, filename='Chart Arrive per Month 2014'))
