"""SMA OF NEXT YEAR 2015"""
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
