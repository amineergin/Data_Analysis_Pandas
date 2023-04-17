import seaborn as sns
df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
print(new_cols)

new_df = df[new_cols]