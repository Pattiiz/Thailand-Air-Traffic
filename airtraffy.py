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
    return static_2014

def fetch_data_2013():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        if run[3] == "2013":
            static_2013.append(run)
    return static_2013

def fetch_data_2012():
    static = open("trafficstatic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2012 = []
    for run in static:
        if run[3] == "2012":
            static_2012.append(run)
    return static_2012

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

def sma_passenger():
    """Return SMA of international passenger of thailand air transporation"""
    import csv
    main_data = csv.reader(open('trafficstatic.csv', newline=''))
    main_data = [row for row in main_data]
    arr_psng = 0
    dep_psng = 0
    tst_psng = 0
    for i in main_data:
        if i[0] == 'BKK' and i[1] == 'Passenger' and i[2] == 'International':
            arr_psng += int(i[6])
            dep_psng += int(i[7])
            tst_psng += int(i[8])
    arr_psng = '%.0f' % (arr_psng / 3)
    dep_psng = '%.0f' % (dep_psng / 3)
    tst_psng = '%.0f' % (tst_psng / 3)
    return [['arrive_inter_passenger', arr_psng], ['departure_inter_passenger', dep_psng]\
            , ['transit_passenger', tst_psng]]
