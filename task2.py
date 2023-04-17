import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() + "_FLAG" for col in df.columns if "NO" not in df.columns]