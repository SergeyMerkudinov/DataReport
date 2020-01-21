import csv
import os
import codecs

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
        return result
