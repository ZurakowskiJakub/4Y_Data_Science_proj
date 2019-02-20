import csv
import statistics
import re
from operator import itemgetter
from collections import OrderedDict

with open('..\\data\\DateAndHoursArrests.csv') as newcsv_file:
    readCSV = csv.reader(newcsv_file, delimiter=',')
    b = 0
    noloc = []
    for d in readCSV:
        ainfo = {
            'Age': '',
            'Sex': '',
            'Race': '',
            'ArrestDate': '',
            'ArrestTime': '',
            'Charge': '',
            'District': '',
            'Neighbourhood': '',
            'Felony': '',
            'Hour': '',
            'Month': ''


        }
        if d and b > 0:
            ainfo['Age'] = d[0]
            ainfo['Sex'] = d[1]
            ainfo['Race'] = d[2]
            ainfo['ArrestDate'] = d[3]

            ainfo['ArrestTime'] = d[4]
            ainfo['Charge'] = d[5]
            ainfo['District'] = d[6]
            ainfo['Neighbourhood'] = d[7]
            ainfo['Felony'] = d[8]
            ainfo['Hour'] = d[9]
            ainfo['Month'] = d[10]
            noloc.append(ainfo)
        b += 1
    Ages = []
    Sexs =[]
    Races =[]
    neighbours = []
    Hours = []
    Felony = []
    RaceFelony = []
    for i in noloc:
        Ages.append(i['Age'])
        Sexs.append(i['Sex'])
        Races.append(str([i['Race']]))
        neighbours.append(i['Neighbourhood'])
        Hours.append(i['Hour'])
        if 'True' in i['Felony']:
            Felony.append(i['Neighbourhood'])
        if 'True' in i['Felony']:
            RaceFelony.append((i['Race']))

    print(Felony)
    agescount = {}
    for i in Ages:
        agescount[i] = agescount.get(i, 0) + 1
    sexscount = {}
    for i in Sexs:
        sexscount[i] = sexscount.get(i, 0) + 1
    racescount = {}
    for i in Races:
        racescount[i] = racescount.get(i, 0) + 1
    neighbourscount = {}
    for i in neighbours:
        neighbourscount[i] = neighbourscount.get(i, 0) + 1
    hoursscount = {}
    for i in Hours:
        hoursscount[i] = hoursscount.get(i, 0) + 1
    felonyscount = {}
    for i in Felony:
        felonyscount[i] = felonyscount.get(i, 0) + 1
    racefelonyscount = {}
    for i in RaceFelony:
        racefelonyscount[i] = racefelonyscount.get(i, 0) + 1
    print(agescount)
    print(sexscount)
    print(racescount)
    print(neighbourscount)
    print(hoursscount)
    print(felonyscount)
    print(racefelonyscount)


    print('HEEEEEEEEERE')
    total = len(noloc)
    sortedages = OrderedDict(sorted(agescount.items(), key=itemgetter(1)))
    print(sortedages)
    sortesexs = OrderedDict(sorted(sexscount.items(), key=itemgetter(1)))
    print(sortesexs)
    sorteraces = OrderedDict(sorted(racescount.items(), key=itemgetter(1)))
    print(sorteraces)
    sortedneighbourhoods = OrderedDict(sorted(neighbourscount.items(), key=itemgetter(1)))
    print(sortedneighbourhoods)
    sortedhours = OrderedDict(sorted(hoursscount.items(), key=itemgetter(1)))
    print(sortedhours)
    sortedfelonys = OrderedDict(sorted(felonyscount.items(), key=itemgetter(1)))
    print(sortedfelonys)
    sortedracefelonys = OrderedDict(sorted(racefelonyscount.items(), key=itemgetter(1)))
    print(sortedracefelonys)
    percentages = {}
    for k, v in sortedneighbourhoods.items():
        small = sortedfelonys.get(k, 0)
        smdec = small / v
        perc = smdec * 100
        percentages[str(k)] = perc
    sortedpercentages = OrderedDict(sorted(percentages.items(), key=itemgetter(1)))

    print(sortedpercentages)

    lowns = []
    for k,v in sortedneighbourhoods.items():
        if v is 1:
            lowns.append(k)

    print(lowns)
    print(percentages['Downtown'])

    print(sorteraces)
    print(total)
    racepercentages = {}
    for k, v in sorteraces.items():
        small = v
        smdec = v / total
        perc = smdec * 100
        racepercentages[str(k)] = perc
    sortedracepercentages = OrderedDict(sorted(racepercentages.items(), key=itemgetter(1)))
    racefelonyspercentages = {}
    for k, v in sortedracefelonys.items():
        small = racescount.get(k,0)
        print(k)
        smdec = v / small
        perc = smdec * 100
        racefelonyspercentages[str(k)] = perc
    sortedracefelonyspercentages = OrderedDict(sorted(racepercentages.items(), key=itemgetter(1)))

    print(sortedracefelonyspercentages)