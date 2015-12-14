"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.tools as tls
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('Pattiiz', 'ph2g5dyom6')

def top_cities():
    """Return top cities"""
    import csv
    main_data = csv.reader(open('trafficstatic.csv', newline=''))
    main_data = [row for row in main_data]
    stat_inter_in = {}
    stat_inter_out = {}
    stat_dome_in = {}
    stat_dome_out = {}
    for i in main_data:
        if i[1] == 'City' and i[2] == 'International':
            stat_inter_in, stat_inter_out = stat_cities(i, stat_inter_in, stat_inter_out)
        elif i[1] == 'City' and i[2] == 'Domestic':
            stat_dome_in, stat_dome_out = stat_cities(i, stat_dome_in, stat_dome_out)
    return ranking(stat_inter_in), ranking(stat_inter_out), ranking(merge(stat_dome_in, stat_dome_out))
    
def stat_cities(data, stat_in, stat_out):
    """Return stats of cities"""
    if data[5] in stat_in:
        stat_in[data[5]] += int(data[6])
    else:
        stat_in[data[5]] = int(data[6])
    if data[5] in stat_out:
        stat_out[data[5]] += int(data[7])
    else:
        stat_out[data[5]] = int(data[7])
    return stat_in, stat_out

def ranking(d_stat):
    """Return cities that ranked"""
    name = sorted(d_stat, key=d_stat.get)
    amount = sorted(list(d_stat.values()))
    stat = []
    pre_stat = []
    for i in range(len(name)):
        pre_stat.append(name[i])
        pre_stat.append(amount[i])
        stat.append(pre_stat)
        pre_stat = []
    return stat

def merge(stat_1, stat_2):
    """Return dic that merge form two dic"""
    stat = {}
    for i in list(stat_1):
        stat[i] = stat_1[i] + stat_2[i]
    return stat

def chart_top_cities_arv_dpt():
    "Create Ring Chart Top Cities International Arrive-Departure Passenger Years 2012-2014"
    top_ten = top_cities()
    cities_2012, cities_2013, cities_2014 = top_ten[0], top_ten[1], top_ten[2]
    fig = {
        "data": [
            {
            "values" : [cities_2012[run][1] for run in range(len(cities_2012)-2,len(cities_2012)-12,-1)],
            "labels" : [cities_2012[run][0] for run in range(len(cities_2012)-2,len(cities_2012)-12,-1)],
            "domain" : {"x": [0, .48]},
            "name" : "Arrive",
            "hoverinfo" : "label+value+name",
            "hole" : .4,
            "type" : "pie"
            },
            {
            "values" : [cities_2013[run][1] for run in range(len(cities_2013)-2,len(cities_2013)-12,-1)],
            "labels" : [cities_2013[run][0] for run in range(len(cities_2013)-2,len(cities_2013)-12,-1)],
            "domain" : {"x": [.52, 1]},
            "name" : "Departure",
            "hoverinfo" : "label+value+name",
            "hole" : .4,
            "type" : "pie"
            },
            ],
        "layout" : {
            "title" : "Top International Cities Arrive/Departure 2012-2014",
            "annotations" : [
                {
                    "font" : {
                        "size" : 20
                    },
                    "showarrow" : False,
                    "text" : "Arrive",
                    "x" : 0.2,
                    "y" : 0.5
                },
                {
                    "font" : {
                        "size" : 20
                    },
                    "showarrow" : False,
                    "text" : "Departure",
                    "x" : 0.83,
                    "y" : 0.5
                }
            ]       
        }            
    }
    return py.plot(fig, filename='Top International Cities Air Traffic 2012-2013')

tls.embed(chart_top_cities_arv_dpt())
