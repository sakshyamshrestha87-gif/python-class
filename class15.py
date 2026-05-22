import pandas as  pd

df = pd.read_csv('output.csv')

new_df = df.dropna()

print(new_df.to_string())


#of.dropna(subset_['Data'], inplace = True)