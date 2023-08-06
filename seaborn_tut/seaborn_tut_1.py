import seaborn as sns

#print(sns.get_dataset_names())
#['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

#plot = sns.load_dataset('tips')
#plot.head()
#print(plot)

import pandas as pd

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

print(data_pd)
