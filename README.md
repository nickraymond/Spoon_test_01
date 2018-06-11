# Spoon_test_01
Test program using Python 3 to open, parse and edit CSV files.

<B>Inputs:

    0872_GPS.csv
    0872_SYS.csv
    
Porgrams

    Spoon_test.py
    Spoon_test_02.py
    
Outputs 
    
    0872_SYS_NEW.csv
    
</B>
    
### Instructions:

The system saves data and log information to its on-board SD card, and for a number of reasons, these logs are broken into several different file types and into indexed chunks. So all logs with prefix of 0872 will cover the same time range, and will have different content for that time range based on the type code (eg SYS or GPS).

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

• Better if the code is easily read by humans, file size not critical

• Assume it is OK to hard code file names into program // if extra time I would like to prompt the user to insert file names

• Output a NEW version of the SYS file with "GPS Epoch Time" added as the second column

• CSV reader only imports values as strings, but we need to covnert some values to floats to perform math

 
### Strategy

1. open NNNN_GPS.csv and NNNN_SYS.csv using the Pandas csv reader to create a DataFrame. I decided to use the Pandas data analysis toolkit because the read_csv method automatically converts numerical values to floats. Additionally, Pandas offers tools to manipulate, add, delete columns in the DataFrames which can be used in place of the dictionaries functionality.

2. Determine when the SYS was last rest in Epoch Time. This linear time offset can be calcuated from the first row in the GPS.csv or any other row for that matter using the SYS and GPS times. It is important to convery the ard_millis value from milliseconds to seconds during the calcualtion. As a quick check, you can calcaulte this offset using row[0]  and then verify with any other row. I did this for row 50 and 100 to verify that the offset value was the same - this represented the time when the SYS clock was last reset.

       ex: epoch_offset = GPS_epoch[0] - ard_millis[0]/1000.0  

3. Apply the linear offset to the entire column of SYS.csv ard_millis data and save the data to a new variable.
       
       ex: sys_epoch_time[i] = ard_millis[i] + epoch_offset
       
4. Add the new column of data to the SYS.csv file, inserting the new data as the second column in the DataFrame. Then save the CSV file with a new name.


### Time Allocation

0. ~30 min to brainstorm, flow chart, and outline assumptions and strategy on paper.
1. ~30 min to setup PyCharm, setting up a virtual environment, and running basic python tutorials from the O'reilly Raspberry Pi Cookbook.
2. ~1 hour learning about CVS readers, lists, dictionaries, and DataFrames and setting up Pandas.
3. 1-2 hours writing code, debugging to create file "Spoon_test.py". At the end of the three hours this program did not have all the functionality that I wanted.
4. ~1 more hour to create Spoon_test_02.py, added user inoputs and check to verify file ID code was the same.
5. Extra - still having fun, decided to setup PyCharm + Github. Created repo to share files.
6. Extra - having too much fun, copied my hand notes to the README file for documentation purposes.

### Process and workflow

##### Q1: how did you approach the problem?

   I had been thinking about this type of problem for some time now, based on my personal project with the small 3D printed wave buoy using an RTC and GPS module. My first task was to list out on paper the goals, my assumptions, and visualize what the final output should look like - including formatting of the new CSV file and the values in the first five rows. The trick was think about how to determine the Epoch time at the moment of the SYS reset. Since the GPS.csv file logged both Epoch and SYS time together, and I assumed that these two times times were sync in a deterministic way, it was possible to calcualte a linear offset  by subtracting the SYS time from the Epoch time for a known entry in the data set. I could then work backward to determine the Epoch time for the reset. If the GPS.csv file had not logged both SYS and Epoch time, then this would be much more difficult since we would need to determine an event when we could safety assume the GPS and SYS clocks were querried at the same moment. 

##### Q2: what steps you go through to learn what options there are?

   I heavily relied upon online resources to get a sense of common tools and strategies. This included Stackoverflow, Youtube, and online tutorials. I also used a book reference, the O'Reilly RPi Cookbook, as this has a chapter on basic Python syntax and example code.  The rest of the task was accomplished by searching StackOverflow for related topics and questions, specific to "user input" or "comparing portions of two strings". Along the way I would create small "test" programs to focus on one small aspect of the code and once that small aspect was working I would then add it to my larger master program. Along the way I kept notes in a google doc with links to helpful tutorials or reference information for quick access.  
 
   
##### Q3:and how you decide between different ways of completing the task? 

   Being that there are some many ways to approach this problem, I first ran through two basic examples for importing/parsing CSV files that repeatedly came up in tutorials and didn't require any that an additional packages be installed. Start with the absolute basics. This discussed parsing the data using either lists or dictionaries. Once I had a grasp on these two options, I tried to modify the values within the ard_millis dataset only to realize that everything had been imported as a string. So I looked for a solution to read csv files as floats, assuming this was more efficient than type casting after parsing everything, and found several references to the Pandas utility. More reading to differentiate why Pandas is better than the basic examples, then I followed two tutorials to learn how to create the DataFrame.
