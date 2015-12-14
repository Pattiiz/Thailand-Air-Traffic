"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('Pattiiz', 'ph2g5dyom6')

def fetch_arrive_2012():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2012 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2012":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2012.append(temporary)
    return static_2012

def summary_arrive_2012():
    "Return Summary Arrive Passenger"
    arrive_2012 = fetch_arrive_2012()
    summary_2012 = {}
    for run in arrive_2012:
        if run[0] in summary_2012:
            summary_2012[run[0]] += int(run[1])
        else:
            summary_2012[run[0]] = int(run[1])
    return summary_2012

def month_list():
    "Create Month list"
    arrive_2012 = fetch_arrive_2012()
    month = []
    for run in range(0, 13):
        month.append(arrive_2012[run][0])
    return month

def chart_arrive_2012():
    "Create Chart Amount International Passenger Arrive per Month Year 2012"
    summary_2012 = summary_arrive_2012()
    month = month_list()
    trace0 = go.Bar(
        x=[run for run in month],
        y=[summary_2012[run] for run in month],
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
        title='International Passengers Arrive per Month - 2012',
    )
    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, filename='International Passengers Arrive per Month - 2012')
    
tls.embed(chart_arrive_2012())
