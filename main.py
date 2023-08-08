import pandas as pd

import functions

url_a = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
url_b = "http://api.nbp.pl/api/exchangerates/tables/b?format=json"

json_a = functions.get_data(url_a)
json_b = functions.get_data(url_b)

df_a = pd.DataFrame(functions.get_rates(json_a))
df_b = pd.DataFrame(functions.get_rates(json_b))

functions.add_params_columns(functions.get_parameters(json_a), df_a)
functions.add_params_columns(functions.get_parameters(json_b), df_b)

combined_df = functions.combine_dataframes(df_a, df_b)

date_a = functions.change_date_format(json_a["effectiveDate"])
date_b = functions.change_date_format(json_b["effectiveDate"])

file_name = date_a + "_" + date_b + ".csv"
combined_df.to_csv(file_name, sep = ",", index = False)
