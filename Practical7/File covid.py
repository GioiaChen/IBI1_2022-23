import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Encounter matplotlib.pyplot for plotting and numpy for useful mathematical functions. 
# Os allows us to work with files and directories, and pandas is for working with dataframes.

os.chdir("C:/cygwin64/home/gioia/IBI1_2022-23")
os.getcwd()
os.listdir()


# Import the .csv file.
covid_data = pd.read_csv("full_data.csv")

covid_data.head(5)
# What does the number 5 do?
# The number 5 means only checking the first 5 lines of the database.

covid_data.info()
covid_data.describe()

covid_data.iloc[0, 1]
covid_data.iloc[2, 0:5]
covid_data.iloc[0:2, :]
covid_data.iloc[0:10:2, 0:5]
covid_data.iloc[0:3, [0, 1, 3]]
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3, my_columns]
covid_data.loc[2:4, "date"]
covid_data.loc[0:, "total_cases"]
covid_data.loc[0:81, "total_cases"]

# Show the second column from every 100th row from the first 1000 rows.
covid_data.iloc[0:1000:100,1]

# Use a Boolean to show “total cases” for all rows corresponding to Afghanistan.
covid_data.loc[covid_data['location'] == "Afghanistan", "total_cases"]
covid_data.loc[0:81, "total_cases"]

# Create a new object called new_data, containing the data of the new_cases and new_deaths of 2020-03-31.
my_columns1 = [False, True, True, True, False, False]
new_data = covid_data.loc[covid_data['date'] == "2020-03-31", my_columns1]

# Compute the mean number of new cases and new deaths on 31 March 2020.
# Be careful to not include the data of the whole world.
x1 = new_data.loc[new_data["location"] != "World", "new_cases"]
print("new_cases ", np.mean(x1))
x2 = new_data.loc[new_data["location"] != "World", "new_deaths"]
print("new_deaths ", np.mean(x2))

# Create the boxplot of new cases and new deaths on 31 March 2020 using new_data.
x = new_data.loc[new_data["location"] != "World", "new_cases"]
y = new_data.loc[new_data["location"] != "World", "new_deaths"]
plt.boxplot((x, y),
            widths=0.3,
            showfliers=False,
            showbox=True,
            labels = ["new cases","new deaths"])
plt.grid(True)
plt.title('2020-03-31')
plt.ylabel('number')
plt.show()

# Draw the plot of world new cases.
world_dates = covid_data.loc[covid_data["location"] == "World", 'date']
world_new_cases = covid_data.loc[covid_data["location"] == "World",'new_cases']
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.yticks([0,10000,20000,30000,40000,50000,60000])
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()

# Draw the plot of Austria total cases and deaths.
austria_date = covid_data.loc[covid_data["location"] == "Austria", 'date']
austria_total_cases = covid_data.loc[covid_data["location"] == "Austria", 'total_cases']
austria_total_deaths = covid_data.loc[covid_data["location"] == "Austria", 'total_deaths']
plt.plot(austria_date, austria_total_deaths, 'ro')
plt.plot(austria_date, austria_total_cases, 'bo')
plt.xticks(austria_date.iloc[0:len(austria_date):4],rotation=-90)
plt.yticks([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()
