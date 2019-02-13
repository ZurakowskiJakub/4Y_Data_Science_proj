import csv
import statistics



with open('BaltimoreNeighbourhoods.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    neighbourhoods= []
    a = 0
    for i in readCSV:

        ninfo = {
            'name' : '',
            'area' : '',
            'population' : '',
            'density' : '',
            'householdincome' : '',
            'rent' : '' ,
            'maleage' : '' ,
            'femaleage' : '' ,

        }
        if i and a > 0 :
            ninfo['name'] = i [0]
            ninfo['area'] = i[1]
            ninfo['population'] = i[2]
            ninfo['density'] = i[3]
            ninfo['householdincome'] = i[4]
            ninfo['rent'] = i[5]
            ninfo['maleage'] = i[6]
            ninfo['femaleage'] = i[7]
            neighbourhoods.append(ninfo)
        a+=1
    totpop = []
    totinc = []
    for i in neighbourhoods:
        totpop.append(int(i['density']))
        totinc.append(int(i['householdincome']))

    medianpop = statistics.median(totpop)/2
    medianinc = statistics.median(totinc)/2
    medpop = statistics.median(totpop)

    medianpoplow = statistics.median(totpop)/5
    #medeianpoplow = medianpoplow * 2
    medianinclow = statistics.median(totinc)/3
    minpop = min(totpop)
    maxpop = max(totpop)

    mininc = min(totinc)
    maxinc = max(totinc)


    incvlow = (mininc + medianinclow)
    inclow = (mininc + medianinc)
    inchigh = (maxinc - medianinc)
    poplow = (minpop + medianpop)
    pophigh =(medpop + (medianpoplow * 3))


    for i in neighbourhoods:
        if float(i['density']) > pophigh:
            i['PopulationRank'] = 'Dense'
        elif float(i['density']) < poplow:
            i['PopulationRank'] = 'Sparse'
        else: i['PopulationRank'] = 'Normal'

        if float(i['householdincome']) > inchigh:
            i['IncomeRank'] = 'Higher'
        elif float(i['householdincome']) < incvlow:
            i['IncomeRank'] = 'VeryLow'
        elif float(i['householdincome']) < inclow:
            i['IncomeRank'] = 'Lower'
        else: i['IncomeRank'] = 'Normal'

    low = 0
    high = 0
    vlow = 0
    for i in neighbourhoods:
        if i['PopulationRank'] is 'Dense':
            high +=1
        elif i['PopulationRank'] is 'Sparse':
            low +=1
        elif i['PopulationRank'] is 'Normal':
            vlow += 1
    print('total :' ,len(neighbourhoods))
    print('higher :', high)
    print('lower :', low)
    print('vlower :', vlow)

    keys = neighbourhoods[0].keys()
    with open('BaltimoreNeighbourhoodsComplete.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(neighbourhoods)


