# Write an operation to find the top 3 batsman who scored 3 runs.

import pandas as pd

df = pd.read_csv('../deliveries.csv')
# data.info()

mask = df['batsman_runs'] == 3
new_df = df[mask]

top3  = new_df.groupby('batsman').size().sort_values(ascending=False).head(3)
print(top3)