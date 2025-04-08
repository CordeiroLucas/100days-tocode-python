import pandas

raw_data = pandas.read_csv("squirrel_census.csv")

organized = raw_data.groupby(by="Primary Fur Color").groups

dict_count = {"Fur Color":[], "Count":[]}

for key in organized:
    dict_count["Fur Color"].append(key)
    dict_count["Count"].append(len(organized[key]))

df = pandas.DataFrame(data=dict_count)
df.to_csv("squirrel_colors.csv")
print(df)


