# Spoon_test_01
Test program using Python 3 to open, parse and edit CSV files.

###Instructions:

The Spotter system saves data and log information to its on-board SD card, and for a number of reasons, these logs are broken into several different file types and into indexed chunks. So all logs with prefix of 0872 will cover the same time range, and will have different content for that time range based on the type code (eg SYS or GPS).

The system has 2 measures of time: 
- one is the on-board system clock count, and describes the time since the last system reset in milliseconds (ard_millis). This clock isn't very accurate in an absolute sense, and will have part-to-part variation, temperature sensitivity, etc. Its usefulness is really for tracking system resets, and for providing a master key to match all the different files to each other. eg:
  • if in a file an event is logged at 10ms, and a 2nd event is logged at 20ms, the difference between those events is only approximately 10ms
  • if in a file an event is logged at 10ms, and in another file an event is logged at 10ms, those events were logged within 1ms of each other.
- the other is a unix timestamp, which is absolute time in seconds since Jan 1st 1970. The unix timestamp is only available once a GPS fix is established, and is only logged to certain file stream types (eg NNNN_GPS.csv). This clock is extremely accurate in an absolute sense, but is only logged in one of the file streams and only when there's an active GPS fix.

### Goals
The goal of the exercise is to write a parsing script in Python that does the following:
- reads NNNN_GPS.csv and NNNN_SYS.csv files from a directory.
- makes sure the NNNN file indexes match.
- uses the GPS file to interpolate epoch timestamps for all the entries in the SYS file based on the ard_millis values.
- saves an edited version of the sys file with an added Gps Epoch Time column.

### Assumptions
    • all csv files are in chronological order // if extra time I would want to verify this
    • NNNN_GPS.csv and NNNN_SYS.csv are taken during the same chunk of time and are sync based on SYS clock
    • better if code is easily read by humnans, file size not critical
    • assume it is OK to hardcode file names into program // if extra time I would like to prompt the user to insert file names
    • output a NEW version of the SYS file with "GPS Epoch Time" added as the second column
    • CSV reader only import values as strings, but we need to covnert some values to floats to perform math

   
  
