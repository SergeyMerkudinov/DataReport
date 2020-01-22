from django.apps import AppConfig

class DataaggregatorConfig(AppConfig):
    name = 'DataAggregator'
    # CSV or API
    DATA_LOAD_METHOD = 'CSV'
    DATA_LOAD_CSV_PARAMS = {'PATH': 'DataAggregator\\data\\CoachData.csv'}
    DATA_LOAD_API_PARAMS = {'PATH': 'https://apidata.mos.ru/v1/datasets/61321/rows', 'API_KEY':'696872ead80adee763a92857f9edd5c1'}
    DATA_LOAD_MAX_RECORDS = 10
