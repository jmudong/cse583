import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

# Reading data file into pd.dataframe
df = pd.read_csv("bicycle_data.csv")

# The dataframe should contain 4 columns, which includes a Date column and a 3 separate columns describing the count
# of bicycles crossing the Fremont Bridge. The Date column should be read as a string (which we can convert into
# a datetime format), while the count columns should be read as an int. 

# Converting Date to datetime format
df["Date"] = pd.to_datetime(df["Date"], format = "%m/%d/%Y %I:%M:%S %p")

# Renaming count columns
df.columns = ["Date", "Total (Hour)", "West", "East"]


# Adding columns to dataframe containing
# 1.) Total (East+West) bicycle count
# 2.) Hour of the day
# 3.) Year 
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year
df["Date"] = df["Date"].dt.date
df["Total (Daily)"] = df.groupby("Date")["Total (Hour)"].transform("sum")

# 2016 subset of original df
df_2016 = df[df["Year"] == 2016]

# Check for missing data
## print(df_2016.isna().any(axis=1).sum())
## 1 row with missing values
# Filter out missing data
df_2016 = df_2016.dropna()   

# Create plot of hour vs. total count

# Calculate average busiest hour of the day
hourly_total_avg = df_2016.groupby("Hour")["Total (Hour)"].mean()
## print((hourly_total_avg.max(), hourly_total_avg.idxmax()))
## Busiest hour is 5pm with ~400 bicycles

print(df.head())


