import matplotlib as plt
import numpy as np 
import pandas as pd 

# Reading data file into pd.dataframe
df = pd.read_csv("bicycle_data.csv")

# The dataframe should contain 4 columns, which includes a Date column and a 3 separate columns describing the count
# of bicycles crossing the Fremont Bridge. The Date column should be read as a string (which we can convert into
# a datetime format), while the count columns should be floats.

# Converting Date to datetime format
df["Date"] = pd.to_datetime(df["Date"], format = "%m/%d/%Y %H:%M:%S %p")


# Adding columns to dataframe containing
# 1.) Total (East+West) bicycle count
# 2.) Hour of the day
# 3.) Year 
