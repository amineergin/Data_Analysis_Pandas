import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = ["NUM_"+ col.upper() for col in df.columns]
