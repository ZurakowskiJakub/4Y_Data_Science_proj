from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import re

def scrapedetails():
    session = requests.Session()

    session.headers.update({'User-Agent': 'Custom user agent'})
    html =session.get('http://www.city-data.com/nbmaps/neigh-Baltimore-Maryland2.html')
    html = html.text
    soup = BeautifulSoup(html, 'html5lib')
    html = session.get('http://www.city-data.com/nbmaps/neigh-Baltimore-Maryland.html')
    html = html.text
    my_soup = BeautifulSoup(html, 'html5lib')

    my_data = []

    for tag in soup.find_all('div', {'class': 'neighborhood'}):
        my_data.append(tag.text)
    for tag in my_soup.find_all('div', {'class': 'neighborhood'}):
        my_data.append(tag.text)

    return my_data

def cleandata(bdata):

    hoodlist = []


    for hood in bdata:
        hoods = {}

        name =  re.search('(.*)neighborhood in Baltimore statistics:',hood)
        area = re.search('Area: (.*) square milesPopulation', hood)
        population = re.search('milesPopulation: (.*)Population density:', hood)
        density = re.search('Population density:(.*) people per square mileBaltimore:7,607', hood)
        householdincome = re.search('household income in 2016:(.*)Baltimore:\$47,350', hood)
        rent = re.search('rent in in 2016:(.*)Baltimore:\$852', hood)
        maleage = re.search('ageMales:(.*)yearsFemales', hood)
        femaleage = re.search('yearsFemales:(.*) yearsHousing', hood)
        dethouses = re.search('(of all units):(.*)Baltimore:\$290,108', hood)
        townhouses = re.search('(of all units):(.*)city:\$187,580', hood)

        if name:  hoods['name'] = name.group(1)
        if hoods: hoods['area'] = area.group(1)
        if population:
            pop = population.group(1)
            newnum = ''.join([n for n in pop if n.isdigit()])
            hoods['population'] = newnum
        if density:
            den = density.group(1)
            dnum = ''.join([n for n in den if n.isdigit()])
            hoods['density'] = dnum

        if householdincome:
            hi = householdincome.group(1)
            income = ''.join([n for n in hi if n.isdigit()])
            hoods['householdincome'] =income

        if rent:
            therent = rent.group(1)
            newrent = ''.join([n for n in therent if n.isdigit()])
            hoods['rent'] = newrent

        if maleage:
            mage = maleage.group(1)
            malage = ''.join([n for n in mage if n.isdigit()])
            malage = int(malage) / 10
            hoods['maleage'] = malage

        if femaleage:
            fage = femaleage.group(1)
            newage = ''.join([n for n in fage if n.isdigit()])

            newage = int(newage)/10
            #newage = str(newage).join('.')
            #newage = newage.join(str(point))

            hoods['femaleage'] = newage

        if dethouses:
            detp = dethouses.group(1)
            newdet = ''.join([n for n in detp if n.isdigit()])
            hoods['dethouses'] = newdet

        if townhouses:
            twn = townhouses.group(1)
            newtown = ''.join([n for n in twn if n.isdigit()])

            hoods['townhouses'] = newtown

        hoodlist.append(hoods)

    print(hoodlist)
    keys = hoodlist[0].keys()
    with open('BaltimoreNeighbourhoods.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(hoodlist)

    return

baltimore_data = scrapedetails()
cleandata(baltimore_data)