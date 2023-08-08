import pandas as pd
import requests
from datetime import datetime


def get_data(url):
    response_api = requests.get(url)
    if response_api.status_code == 200:
        return response_api.json()[0]
    else:
        return None


def get_rates(dataset_dict):
    return dataset_dict.get('rates')


def get_parameters(dataset_dict):
    parameters_dict = {key : dataset_dict[key] for key in set(list(dataset_dict.keys())) - {'rates'}}
    return parameters_dict


def add_params_columns(parameters_dict, pandas_dataframe):
    for elem in parameters_dict:
        pandas_dataframe.insert(0, elem, parameters_dict[elem])


def combine_dataframes(*dataframes):
    return pd.concat(dataframes).reset_index(drop = True)


def change_date_format(date_format_with_dashes):
    return datetime.strptime(date_format_with_dashes, "%Y-%m-%d").strftime("%d %B %Y")