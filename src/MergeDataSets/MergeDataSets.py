import re
import csv


with open('..\\Clean_Offence_Table\\output.csv') as csv_file:
    offencecsv = csv.reader(csv_file, delimiter=',')

    with open(
            '..\\..\\data\\BPD_Arrests_Without_Blank_Locations.csv') as csv_file:
        arrestscsv = csv.reader(csv_file, delimiter=',')

        fullarrest = []
        for arrest in arrestscsv:
            arrest[9] = arrest[9].replace(" ", "")
            ainfo = {
                'Age:': '',
                'Sex': '',
                'Race': '',
                'ArrestDate': '',
                'ArrestTime': '',
                'ArrestLocation': '',
                'IncidentLocation': '',
                'Charge': '',
                'District': '',
                'Neighbourhood': '',
                'Longitude': '',
                'Latitude': '',
                'Location1': ''

            }


            ainfo['Age'] = arrest[1]
            ainfo['Sex'] = arrest[2]
            ainfo['Race'] = arrest[3]
            ainfo['ArrestDate'] = arrest[4]
            ainfo['ArrestTime'] = arrest[5]
            ainfo['ArrestLocation'] = arrest[6]

            ainfo['IncidentLocation'] = arrest[8]
            ainfo['Charge'] = arrest[9]

            ainfo['District'] = arrest[11]

            ainfo['Neighbourhood'] = arrest[13]
            ainfo['Longitude'] = arrest[14]
            ainfo['Latitude'] = arrest[15]
            ainfo['Location1'] = arrest[16]

            fullarrest.append(ainfo)

        offencelist = []

        for offence in offencecsv:
            if offence:
                offence[0] = offence[0].replace('-', "")
                offencelist.append(offence)

        fulloffence = []
        for offence in offencelist:
            if offence[2]:
                fulloffence.append(offence)
        for offence in fulloffence:
            offence[0] =re.findall(r'\d+', offence[0])

            if offence[0]:
                offence[0] = str(offence[0][0])

        for arrest in fullarrest:
            for offence in fulloffence:

                if str(offence[0])in str(arrest['Charge']) :
                    arrest['Felony'] = str(offence[2])
                    break
                else:
                    arrest['Felony'] = ''


        finalarrest = []
        for arrest in fullarrest:

            if arrest['Felony']:
                if 'Misd.' in arrest['Felony']  :
                    arrest['Felony'] = False
                    finalarrest.append(arrest)
                elif 'Felony' in arrest['Felony']:
                    arrest['Felony'] = True
                    finalarrest.append(arrest)

        print(finalarrest)
        keys = finalarrest[0].keys()

        with open('..\\..\\data\\heatmapdata.csv', 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(finalarrest)

        noloc = []
        for i in finalarrest:
            ainfo = {
                'Age': '',
                'Sex': '',
                'Race': '',
                'ArrestDate': '',
                'ArrestTime': '',
                'Charge': '',
                'District': '',
                'Neighbourhood': '',
                'Felony' : ''

            }

            ainfo['Age'] = i['Age']
            ainfo['Sex'] = i['Sex']
            ainfo['Race'] = i['Race']
            ainfo['ArrestDate'] = i['ArrestDate']
            ainfo['ArrestTime'] = i['ArrestTime']
            ainfo['Charge'] = i['Charge']
            ainfo['District'] = i['District']
            ainfo['Neighbourhood'] = i['Neighbourhood']
            ainfo['Felony'] = i['Felony']

            noloc.append(ainfo)
            
        keys = noloc[0].keys()
        with open('..\\..\\data\\finaldataset.csv', 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(noloc)





