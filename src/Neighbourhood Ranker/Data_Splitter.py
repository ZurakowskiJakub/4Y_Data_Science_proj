
import csv
import statistics
import re

with open('BaltimoreNeighbourhoodsComplete.csv') as csv_file:
    readCSV1 = csv.reader(csv_file, delimiter=',')

    neighbourhoods= []
    a = 0
    for i in readCSV1:

        ninfo = {
            'name' : '',
            'area' : '',
            'population' : '',
            'density' : '',
            'householdincome' : '',
            'rent' : '' ,
            'maleage' : '' ,
            'femaleage' : '' ,
            'PopulationRank' : '' ,
            'IncomeRank' : ''

        }
        if i and a > 0 :

            ninfo['name'] = i[0]
            ninfo['area'] = i[1]
            ninfo['population'] = i[2]
            ninfo['density'] = i[3]
            ninfo['householdincome'] = i[4]
            ninfo['rent'] = i[5]
            ninfo['maleage'] = i[6]
            ninfo['femaleage'] = i[7]
            ninfo['PopulationRank'] = i[8]
            ninfo['IncomeRank'] = i[9]
            neighbourhoods.append(ninfo)
        a+=1

    with open('..\\..\\data\\finaldataset.csv') as newcsv_file:
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
                'Felony': ''

            }
            if d and b > 0:

                ainfo['Age'] = d[0]
                ainfo['Sex'] = d[1]
                ainfo['Race'] = d[2]
                ainfo['ArrestDate'] = d[3]
                x = re.split(":", d[4], 1)
                ainfo['Hour'] = x[0]
                y = re.split("/", d[3])
                ainfo['Month'] = y[1]
                ainfo['ArrestTime'] = d[4]
                ainfo['Charge'] = d[5]
                ainfo['District'] = d[6]
                ainfo['Neighbourhood'] = d[7]
                ainfo['Felony'] = d[8]

                noloc.append(ainfo)
            b+=1


        densen = []
        lowinc = []

        for i in neighbourhoods:

            if 'Dense' in i['PopulationRank']:
                densen.append(i)
            if 'VeryLow' in i['IncomeRank']:
                lowinc.append(i)

        hidas = []
        for i in noloc:
            for n in densen:
                if i['Neighbourhood'] in n['name']:
                    hidas.append(i)
        lowincas = []
        for i in noloc:
            for n in lowinc:
                if i['Neighbourhood'] in n['name']:
                    lowincas.append(i)

        keys = noloc[0].keys()
        print(keys)
        with open('..\\..\\data\\DateAndHoursArrests.csv', 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(noloc)


        keys = lowincas[0].keys()
        print(keys)
        with open('..\\..\\data\\LowIncomeArrests.csv', 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(lowincas)

        keys = hidas[0].keys()
        with open('..\\..\\data\\HighDensityArrests.csv', 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(hidas)
