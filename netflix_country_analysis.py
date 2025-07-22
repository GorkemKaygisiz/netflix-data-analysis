import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("C:\\Users\\Görkem\\Desktop\\data_ex\\netflix_cleaned_data.csv")


#2025 yılında Netflix'e en çok içerik ekleyen 5 ülkeyi bul ve çubuk grafikle göster

data= data[data["year_added"]==2020]

data["country"] = data["country"].str.split(",")


data=data.explode("country")
data["country"] = data["country"].str.strip()
data = data[data["country"] != "Unknown"]
grouped_data = data.groupby(["country","year_added"]).size().unstack(fill_value=0)


totals=grouped_data.sum(axis=1)  #Calculate total number of contents per country
top_5 = totals.sort_values(ascending=False).head(5)


plt.figure()
plt.title("Top 5 Countries by Number of Titles Added in 2020")
plt.xlabel("Countries")
plt.xticks(rotation=45)
plt.ylabel("Number of Title")
plt.bar(top_5.index,top_5.values)
plt.show()