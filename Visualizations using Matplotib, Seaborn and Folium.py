import matplotlib

import matplotlib.pyplot as plt
import requests
import io
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# URL of the CSV file
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv"

# Fetch the data from the URL
response = requests.get(URL)

# Raise an error if the request failed
response.raise_for_status()

# Convert the response content into a readable format for pandas
csv_content = io.StringIO(response.text)
# Read the CSV data into a pandas dataframe
df = pd.read_csv(csv_content)

#print(df.columns)

##TASK 1.1
# Develop a Line chart using the functionality of pandas to show how Average automobile sales fluctuate from year to year

plt.figure(figsize = (10,6))
df_line= df.groupby('Year')['Automobile_Sales'].mean()
df_line.plot(kind='line',x=df_line.index,y=df_line.values)
plt.xlabel('Year')
plt.ylabel('Sales Volume')
plt.title('Automobile Sales Over Time')
plt.text(2007,650, "Recession")
plt.legend()
#plt.show()

print(df_line.head())


#
#TASK 1.2:
# How do trends in advertising expenditure correlate with automobile sales during non-recession periods, and what insights can be derived from this relationship.

df_no_regression = df[df['Recession'] == 0]
grouped_data = df_no_regression.groupby('Year')[['Automobile_Sales', 'Advertising_Expenditure']].mean().reset_index()

# 3. Tworzenie wykresu
plt.figure(figsize=(10, 6))

# Linia dla średniej sprzedaży samochodów (zielona, ciągła, okrągłe znaczniki)
sns.lineplot(data=grouped_data, x='Year', y='Automobile_Sales',
             color='green', marker='o', label='Avg Automobile Sales')

# Linia dla średnich wydatków na reklamę (niebieska, przerywana, kwadratowe znaczniki)
sns.lineplot(data=grouped_data, x='Year', y='Advertising_Expenditure',
             color='blue', linestyle='--', marker='s', label='Avg Advertising Expenditure')

# 4. Dodanie etykiet, tytułu, legendy i siatki
plt.title('Trends in Advertising Expenditure and Automobile Sales (Non-Recession Periods)')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
#plt.show()

#TASK 1.3
#Compare the sales of different vehicle types during a recession and a non-recession period
df_compare = df.groupby(['Recession','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
print((df_compare.head()))

# Creating the grouped bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Recession', y='Automobile_Sales',hue='Vehicle_Type', data=df_compare)
plt.xlabel('Period')
plt.ylabel('Average Sales')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
plt.legend(title='Vehicle Type')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.tight_layout()
plt.savefig("Bar_Chart.png")
plt.show()

#TASK 1.4
#Scatter plot to identify the relationship between consumer confidence and automobile sales during recessions
df_recession = df[df['Recession'] == 1]
plt.figure(figsize=(10, 6))
plt.scatter(df_recession['Consumer_Confidence'],df_recession['Automobile_Sales'])
plt.title(" Relationship between consumer confidence and automobile sales during recessions ")
plt.xlabel('Consumer Confidence')
plt.ylabel('Automobile Sales')
plt.show()

#TASK1.5
# Develop a pie plot to display see the total Automobile_Sales for each vehicle during recession period

df_veh = df_recession.groupby('Vehicle_Type')['Automobile_Sales'].sum()
plt.figure(figsize=(10, 6))
labels = df_veh.index
sizes = df_veh.values
plt.pie(sizes, labels = labels, autopct='%1.1f%%',
        shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9},startangle=90)

plt.title('Share of Each Vehicle Type in Total Sales during Recessions')

plt.show()
