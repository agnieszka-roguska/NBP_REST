import unittest
import functions
import pandas as pd
from pandas.testing import assert_frame_equal


class NBP_Tests(unittest.TestCase):
    def test_get_rates_when_you_pass_json_it_returns_column_with_rates(self):
        dataset = {'label_1' : 'sth_1', 'label_2': 3, 'rates' : [{"rate_1" : "currency", "code" : "1"}, {"rate_2" : "currency_2", "code" : "2"}]}
        result = functions.get_rates(dataset)
        expected = [{"rate_1" : "currency", "code" : "1"}, {"rate_2" : "currency_2", "code" : "2"}]
        self.assertEqual(expected, result)

    def test_get_parameters_when_you_pass_dataset_it_returns_all_elements_that_are_not_lists_of_objects(self):
        dataset = {'label_1' : 'sth_1', 'label_2': 3, 'rates' : [{"rate_1" : "currency", "code" : "1"}, {"rate_2" : "currency_2", "code" : "2"}]}
        result = functions.get_parameters(dataset)
        expected = {'label_1' : 'sth_1', 'label_2': 3}
        self.assertEqual(expected, result)

    def test_add_params_columns(self):
        parameters_dict = {'label_3' : 'sth_1', 'label_4': 3}
        pandas_dataframe = pd.DataFrame({'label_1' : ['sth_1', 1, '212'], 'label_2': [3, 4, 5]})
        functions.add_params_columns(parameters_dict, pandas_dataframe)
        result = pandas_dataframe
        expected = pd.DataFrame({'label_4' : [3, 3, 3],'label_3' : ['sth_1', 'sth_1', 'sth_1'], 'label_1' : ['sth_1', 1, '212'], 'label_2': [3, 4, 5]})
        assert_frame_equal(expected, result)

    def test_combine_dataframes_takes_two_pandas_dataframes_and_returns_one_dataframe_consists_of_two_given(self):
        dataframe_1 = pd.DataFrame({'label_1' : ['sth_1', 1, '212'], 'label_2': [3, 4, 5]})
        dataframe_2 = pd.DataFrame({'label_1' : [2, 1.01], 'label_2': ['False', 'True']})
        result = functions.combine_dataframes(dataframe_1, dataframe_2)
        expected = pd.DataFrame({'label_1' : ['sth_1', 1, '212', 2, 1.01], 'label_2': [3, 4, 5, 'False', 'True']})
        assert_frame_equal(expected, result)

    def test_change_date_format_takes_date_in_format_ddmmyyy_separated_by_dashes_and_returns_date_in_human_readable_format(self):
        date = '2019-08-10'
        result = functions.change_date_format(date)
        expected = '10 August 2019'
        self.assertEqual(expected, result)