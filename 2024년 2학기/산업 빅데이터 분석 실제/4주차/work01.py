import pandas as pd
movies_df = pd.read_csv("D:/IMDB-Movie-Data.csv",
index_col="Title")

print(movies_df)