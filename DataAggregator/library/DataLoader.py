import csv
import os
import codecs
import json
import urllib.request
from urllib.error import URLError

from DataAggregator.apps import DataaggregatorConfig
from DataAggregator.models import Coach

from DataReport.settings import BASE_DIR


class DataLoader:
    loadMethod = ''

    def __init__(self, configObject):
        self.loadMethod = configObject.DATA_LOAD_METHOD

    def extract(self, maxRecords=-1):
        result = list()

        if self.loadMethod == 'CSV':
            csvFilePath = os.path.join(BASE_DIR, DataaggregatorConfig.DATA_LOAD_CSV_PARAMS['PATH'])
            try:

                with codecs.open(csvFilePath, encoding='utf-8') as csvfile:
                    buffer = csv.reader(csvfile)
                    headers = next(buffer)
                    i = 0
                    for row in buffer:
                        if i >= maxRecords and maxRecords != -1:
                            break
                        else:
                            currentCoach = dict(zip(headers, row))
                            result.append(Coach(
                                id=currentCoach['ID'],
                                firstName=currentCoach['Name'],
                                lastName=currentCoach['LastName'],
                                secondName=currentCoach['MiddleName'],
                                gender=currentCoach['Gender'],
                                birthDate=currentCoach['DateOfBirth'],
                                sport=currentCoach['SportName'],
                                seniorityPeriod=currentCoach['SeniorityPeriod'],
                                citizenship=currentCoach['Citizenship'],
                                publicPhone=currentCoach['PublicPhone'],
                                email=currentCoach['Email'],
                                jobInfo=currentCoach['JobOrganizationName']
                            ))
                            i += 1
            except FileNotFoundError:
                print("Unable to load CSV file in repository. Check AppSettings for the correct path")

        if self.loadMethod == 'API':
            # Firstly we need to call api to retrieve data
            try:
                apiUrl = DataaggregatorConfig.DATA_LOAD_API_PARAMS['PATH'] + '?' + '$top=' + str(DataaggregatorConfig.DATA_LOAD_MAX_RECORDS) + '&api_key=' + DataaggregatorConfig.DATA_LOAD_API_PARAMS['API_KEY']
                response = urllib.request.urlopen(apiUrl).read().decode('utf-8')
                response = json.loads(response)
                for currentCoach in response:
                    result.append(Coach(
                        id=currentCoach['Number'],
                        firstName=currentCoach['Cells']['Name'],
                        lastName=currentCoach['Cells']['LastName'],
                        secondName=currentCoach['Cells']['MiddleName'],
                        gender=currentCoach['Cells']['Gender'],
                        birthDate=currentCoach['Cells']['DateOfBirth'],
                        sport=currentCoach['Cells']['Sport'][0]['SportName'],
                        seniorityPeriod=currentCoach['Cells']['Sport'][0]['SeniorityPeriod'],
                        citizenship=currentCoach['Cells']['Citizenship'][0]['Citizenship'],
                        publicPhone=currentCoach['Cells']['PublicPhone'][0]['PublicPhone'],
                        email=currentCoach['Cells']['Email'][0]['Email'],
                        jobInfo=currentCoach['Cells']['JobOrganisation'][0]['JobOrganizationName']
                    ))

            except URLError:
                print("Unable to connect and retrieve data from an external system")

        return result
