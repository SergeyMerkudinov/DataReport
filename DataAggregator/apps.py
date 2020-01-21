from django.apps import AppConfig

class DataaggregatorConfig(AppConfig):
    name = 'DataAggregator'
    DATA_LOAD_METHOD = 'CSV'
    DATA_LOAD_CSV_PARAMS = {'PATH': 'DataAggregator\\data\\CoachData.csv'}
    DATA_LOAD_API_PARAMS = {'PATH': ''}
    DATA_LOAD_MAX_RECORDS = 20
