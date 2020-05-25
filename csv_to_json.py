import pandas as pd
import json

#Put the path to the location of the data, in CSV format inside the quotes below
data_df = pd.read_csv('')

with open("data/current_data.json", "w") as f:
    json.dump({"data": data_df.astype(str).values.tolist()}, f, indent=2)