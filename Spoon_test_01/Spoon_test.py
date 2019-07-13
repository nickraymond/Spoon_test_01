# File name : Spoon_test.py
# Creator : Nick Raymond
# Date : June 10, 2018
# Description : code after 3 hour hard stop

import pandas as pd

print('\n\nRunning file : Spoon_test.py\n\n\n')

# prompt the user to select two input files
# <code goes here>

# Read the NNNN_GPS.csv with pandas into a dataFrame
df1 = pd.read_csv('0872_GPS.CSV')

# Read the NNNN_SYS.cvs with pandas into a dataFrame
df2 = pd.read_csv('0872_SYS.CSV')

# Check that NNNN matches from both files by looking at first four charecters file names
# <code goes here>

# Print the first five rows of the GPS data, to see headers + 4 rows of data for a check
print(df1.head())

# print the first five rows of the GPS data, to see headers + 4 rows of data for a check
print(df2.head())

# Check that NNNN matches from both files by looking at first four charecters file names
# <code goes here>


# Determine the Epoch time of the last SYS reset, remember to convert millis to seconds
epoch_time = float(df1.loc[0,"GPS Epoch Time"]) - float(df1.loc[0, "ard_millis"])/1000.0

print("\n\nThe last system reset occurred at:", epoch_time, "Epoch Time.\n\n")

# create a new column of data and add the value epoch_time to all entries in ard_millis SYS column
sys_epoch_time = df2.loc[:,"ard_millis"]/1000.0 + epoch_time

# verify this worked as expected
print(sys_epoch_time)

# add the new column of data to the df2 dataFrame after the ard_millis column
idx = 1
new_col = sys_epoch_time
df2.insert(loc=idx, column='GPS Epoch Time', value=new_col)

# Save dataFrame as csv in the working director, do not include the dataFrame index
new_file_name = '0872_SYS_2.csv'
df2.to_csv(new_file_name, index=False)

# # check - open the CSV we just made and look at the header
# # read the GPS csv with panda into a dataFrame

