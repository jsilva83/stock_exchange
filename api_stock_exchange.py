# Import python modules.
import os
import requests
import itertools


class StockExchange:

    def __init__(self, company_symbol: str):
        """Initialize th object with the company symbol the user wants to get the data.
        :param company_symbol: (str) The company symbol to get data. Example: TSLA stands for TESLA.
        """
        # API input parameters.
        self.company_symbol = company_symbol
        self.url = 'https://www.alphavantage.co/query'
        self.my_alphavantage_api_key = os.environ.get('MY_ALPHAVANTAGE_API_KEY')
        if self.my_alphavantage_api_key is None:
            import api_keys
            self.my_alphavantage_api_key = api_keys.MY_ALPHAVANTAGE_API_KEY
        return

    def get_last_2_days(self) -> dict:
        # API input parameters.
        alpha_parameters = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': self.company_symbol,
            'outputsize': 'compact',
            'datatype': 'json',
            'apikey': self.my_alphavantage_api_key,
        }
        alpha_response = requests.get(url=self.url, params=alpha_parameters)
        alpha_response.raise_for_status()
        alpha_data_json = alpha_response.json()
        # Get only data dictionary with daily values.
        data_dict_1 = alpha_data_json['Time Series (Daily)']
        # Get only 2 first elements of the daily values.
        data_dict_2 = dict(itertools.islice(data_dict_1.items(), 2))
        return data_dict_2
