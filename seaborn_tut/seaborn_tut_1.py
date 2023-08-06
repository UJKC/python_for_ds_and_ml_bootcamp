import seaborn as sns

print(sns.get_dataset_names())
plot = sns.load_dataset('tips')
plot.head()
print(plot)