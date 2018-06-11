# File name : Spoon_test_02.py
# Creator : Nick Raymond
# Date : June 10, 2018

import pandas as pd
import sys


print('\n\nRunning file : Spoon_test_02.py\n\n\n')

# prompt the user to select two input files
file_name_GPS = input('Please enter the filename for GPS data:')
file_name_SYS = input('Please enter the filename for SYS data:')

# Check that NNNN matches from both files by looking at first four char in file names
if file_name_GPS[0:4] == file_name_SYS[0:4]:
    print('\nThe file IDs match!\n')
else:
    sys.exit('error - file IDs do not match!')

# Read the cvs files into a pandas dataFrame, we can use header names as references
df1 = pd.read_csv(file_name_GPS)
df2 = pd.read_csv(file_name_SYS)

# Check the first five rows of the parsed data, to see headers + 4 rows of data
print(df1.head())
print(df2.head())



# Determine the Epoch time of the last SYS reset, remember to convert millis to seconds
epoch_time = float(df1.loc[0,"GPS Epoch Time"]) - float(df1.loc[0, "ard_millis"])/1000.0

print("\n\nThe last system reset occurred at:", epoch_time, "Epoch Time.\n\n")

# create a new column of data and add the value epoch_time to all entries in ard_millis SYS column
sys_epoch_time = df2.loc[:,"ard_millis"]/1000.0 + epoch_time

# add the new column of data to the df2 dataFrame after the ard_millis column
idx = 1
new_col = sys_epoch_time
df2.insert(loc=idx, column='SYS Epoch Time', value=new_col)

# Save dataFrame as csv in the working director, do not include the dataFrame index
new_file_name = file_name_SYS[0:4] + '_SYS_NEW.csv'
df2.to_csv(new_file_name, index=False)
print('Created new file with the name:', new_file_name)