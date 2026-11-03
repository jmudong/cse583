After creating the necessary directories and obtaining the data file, I first wanted to create a 
.gitignore file so that I could avoid pushing the CSV file to my repository. 

Then, I read in the data as a pd.DataFrame, and decided to convert the Date column - which was 
originally a string - into a pd.DataTime format. From my brief understanding, datetime.datetime
is a traditional way of specifying a specific datetime format type, while np.datetime allows for
vectorized calculations of datetime objects. I decided to use the pd.DateTime format because I
was already working with a pandas dataframe, and it also allowed me to specify the datetime
format that I was working with.

Because I converted Date into a datetime column, extracting the Hour and the Year and
adding them as separate columns was very easy to do. I did not decide to add another column
for the Total number of bikes, since this was already included with the original data and I
verified that this was indeed the column of interest by performing a fairly quick logical
operator test. 

Afterwards, I subset the data to only data from 2016, filtered out the missing values, and
used matplotlib to create a line plot of Total Bicycle Count vs. Hour. 

To calculate the average count of each hour, I used the groupby function to perform
aggregate calculations for each hour, and used the max and idxmax functions to return
the hour of the day with the highest average total count.
