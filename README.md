# Spoon_test_01
Test program using Python 3 to open, parse and edit CSV files.

### Instructions:

The Spotter system saves data and log information to its on-board SD card, and for a number of reasons, these logs are broken into several different file types and into indexed chunks. So all logs with prefix of 0872 will cover the same time range, and will have different content for that time range based on the type code (eg SYS or GPS).

The system has 2 measures of time: 
- One is the on-board system clock count, and describes the time since the last system reset in milliseconds (ard_millis). This clock isn't very accurate in an absolute sense, and will have part-to-part variation, temperature sensitivity, etc. Its usefulness is really for tracking system resets, and for providing a master key to match all the different files to each other. eg:
  
• If in a file an event is logged at 10ms, and a 2nd event is logged at 20ms, the difference between those events is only approximately 10ms
  
• If in a file an event is logged at 10ms, and in another file an event is logged at 10ms, those events were logged within 1ms of each other.

- The other is a unix timestamp, which is absolute time in seconds since Jan 1st 1970. The unix timestamp is only available once a GPS fix is established, and is only logged to certain file stream types (eg NNNN_GPS.csv). This clock is extremely accurate in an absolute sense, but is only logged in one of the file streams and only when there's an active GPS fix.

### Goals
The goal of the exercise is to write a parsing script in Python that does the following:
- Reads NNNN_GPS.csv and NNNN_SYS.csv files from a directory.
- Makes sure the NNNN file indexes match.
- Uses the GPS file to interpolate epoch timestamps for all the entries in the SYS file based on the ard_millis values.
- Saves an edited version of the sys file with an added Gps Epoch Time column.

### Assumptions
• All csv files are in chronological order // if extra time I would want to verify this

• NNNN_GPS.csv and NNNN_SYS.csv are taken during the same chunk of time and are sync based on SYS clock

• Better if the code is easily read by humnans, file size not critical

• Assume it is OK to hardcode file names into program // if extra time I would like to prompt the user to insert file names

• Output a NEW version of the SYS file with "GPS Epoch Time" added as the second column

• CSV reader only imports values as strings, but we need to covnert some values to floats to perform math

 
### Strategy

1. open NNNN_GPS.csv and NNNN_SYS.csv using the Pandas csv reader to create a DataFrame. I decided to use the Pandas data analysis toolkit because the read_csv method automatically converts numerical values to floats. Additionally, Pandas offers tools to manipulate, add, delete columns in the DataFrames which can be used in place of the dictionaries functionality.

2. Determine when the SYS was last rest in Epoch Time. This linear time offset can be calcuated from the first row in the GPS.csv or any other row for that matter using the SYS and GPS times. It is important to convery the ard_millis value from milliseconds to seconds during the calcualtion.

       ex: epoch_offset = GPS_epoch[0] - ard_millis[0]/1000.0  

3. Apply the linear offset to the entire column of SYS.csv ard_millis data and save the data to a new variable.
       
       ex: sys_epoch_time[i] = ard_millis[i] + epoch_offset
       
4. Add the new column of data to the SYS.csv file, inserting the new data as the second column in the DataFrame. Then save the CSV file with a new name.


### Time Allocation

0. Approximatly 30 min to brainstorm, flow chart, and outline assumptions and strategy on paper.
1. Approximatly 30 min to setup PyCharm, setting up a virtual environment, and running basic python tutorials from the O'reilly Raspberry Pi Cookbook.
2. Approximatly one hour learning about CVS readers, lists, dictionaries, and DataFrames and setting up Pandas.
3. Approximatly 1 - 2 hours writting code, debugging to create file "Spoon_test.py". At the end of the three hours hard stop this program did not have all the functionality that I wanted.
4. Approximatly 1 more hour to create Spoon_test_02.py, added user inoputs and check to verify file ID code was the same.
5. Extra - having too much fun, decided to setup PyCharm + Github. Created repo to share files.
6. Extra - still having fun, added my notes to the README file.