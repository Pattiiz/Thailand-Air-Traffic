"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
def fetch_data_2014():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        if run[3] == "2014":
            static_2014.append(run)

def fetch_data_2013()
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        if run[3] == "2013":
            static_2013.append(run)

def fetch_data_2012()
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2012 = []
    for run in static:
        if run[3] == "2012":
            static_2012.append(run)
