# Pandas

# import pandas as Pd
# csv_panda_df = Pd.read_table(r"/Users/default/Downloads/Text Files/m.txt" , sep="\t     \t") # ,  header = None  , names = ["Year" , "Price" , "WinterRain" ])
# print(csv_panda_df)

# taxt, excel, csv, json files

# import pandas as Pd
# df = Pd.read_excel(r"/Users/default/Downloads/Excel Files/Apocolypse Food Prep - Drill Down Tutorial.xlsx")
# Pd.set_option("display.max.rows" , 85)
# # print(df)
# print(df.info())
# print(df.shape)
# print(df.tail(5))
# print(df.iloc[83])


import pandas as Pd
df = Pd.read_csv(r"/Users/default/Downloads/CSV Files/world_population.csv")
# Pd.set_option("display.max.columns", 18)
# print(df)

print(df[df["Rank"] < 10])
specific_countries = ["Bangladesh" , "Brazil" , 'Russia' , "United States"]

print(df[df["Country/Territory"].isin(specific_countries)])
print(df[df["Country/Territory"].str.contains("United")])

