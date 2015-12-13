"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('Pattiiz', 'ph2g5dyom6')

def fetch_arrive_2012():
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
    arrive_2012 = fetch_arrive_2012()
    summary_2012 = {}
    for run in arrive_2012:
        if run[0] in summary_2012:
            summary_2012[run[0]] += int(run[1])
        else:
            summary_2012[run[0]] = int(run[1])
    return summary_2012

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
            summary_2014[run[0]] += int(run[1])
        else:
            summary_2014[run[0]] = int(run[1])
    return summary_2014

def average_arrive():
    summary_2012 = summary_arrive_2012()
    summary_2013 = summary_arrive_2013()
    summary_2014 = summary_arrive_2014()
    month = month_list()
    average_arv = []
    temporary = 0
    for run in month:
        temporary = 0
        temporary = (int(summary_2012[run]) + int(summary_2013[run]) + int(summary_2014[run]))//3
        average_arv.append(temporary)
    return average_arv

def fetch_departure_2012():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2012 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2012":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2012.append(temporary)
    return static_2012

def summary_departure_2012():
    departure_2012 = fetch_departure_2012()
    summary_2012 = {}
    for run in departure_2012:
        if run[0] in summary_2012:
            summary_2012[run[0]] += int(run[1])
        else:
            summary_2012[run[0]] = int(run[1])
    return summary_2012

def fetch_departure_2013():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2013":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2013.append(temporary)
    return static_2013

def summary_departure_2013():
    departure_2013 = fetch_departure_2013()
    summary_2013 = {}
    for run in departure_2013:
        if run[0] in summary_2013:
            summary_2013[run[0]] += int(run[1])
        else:
            summary_2013[run[0]] = int(run[1])
    return summary_2013

def fetch_departure_2014():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2014":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2014.append(temporary)
    return static_2014

def summary_departure_2014():
    departure_2014 = fetch_departure_2014()
    summary_2014 = {}
    for run in departure_2014:
        if run[0] in summary_2014:
            summary_2014[run[0]] += int(run[1])
        else:
            summary_2014[run[0]] = int(run[1])
    return summary_2014

def average_departure():
    summary_2012 = summary_departure_2012()
    summary_2013 = summary_departure_2013()
    summary_2014 = summary_departure_2014()
    month = month_list()
    average_dpt = []
    temporary = 0
    for run in month:
        temporary = 0
        temporary = (int(summary_2012[run]) + int(summary_2013[run]) + int(summary_2014[run]))//3
        average_dpt.append(temporary)
    return average_dpt

def month_list():
    departure_2012 = fetch_departure_2012()
    month = []
    for run in range(0, 13):
        month.append(departure_2012[run][0])
    return month

average_arv = average_arrive()
average_dpt = average_departure()
month = month_list()
trace0 = go.Bar(
    x=[run for run in month],
    y=[run for run in average_arv],
    name='Arrive',
    marker=dict(
        color='rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x=[run for run in month],
    y=[run for run in average_dpt],
    name='Departure',
    marker=dict(
        color='rgb(204,204,204)',
    )
)
data = [trace0, trace1]
layout = go.Layout(
    title='Chart Arrive-Departure Average 2012-2014',
    xaxis=dict(
        tickangle=-45,
    ),
    barmode='group',
)
fig = go.Figure(data=data, layout=layout)
tls.embed(py.plot(fig, filename='Chart Arrive-Departure Average 2012-2014'))
