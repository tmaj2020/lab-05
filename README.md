# Lab 5
Clone this repo to your machine to get started!

## Team Members
- Ty Benjamin Majam
- Richard Oh (Worked on questions together)

## Lab Question Answers

Answer for Question 1: 
DBm is decibel-milliwatts, a unit used to measure power. Signal strength is proportional to link speed, which means that higher values are considered better.


Answer for Question 2:
We need to check the OS since each OS may have different methods or commands that need to be called to check the signal level. The difference between these commands appear to mainly be syntax based, but they also appear to have different names for the signal level since Linux has it listed as “Signal level=(-?\d+) dBm”, Windows has it as “Signal\s*:\s*(\d+)%” and Mac has it listed as “agrCtlRSSI:\s*(-?\d+)”


Answer for Question 3:
Subprocess.check_output() appears to be running a command within the shell of the computer running this program and returns the output of that command in the form of a utf-8 encoded object.


Answer for Question 4:
Re.search appears to look through the output object that was received from subprocess.check_output, and is looking for a specific line of information from that object after it is decoded from utf-8. This command should return the matching object and none if there isn’t a match found.


Answer for Question 5:
We need to convert the signal quality not necessarily to dBm, but to the actual RSSI signal in dBm. This is because of how the signal is returned as percentage, where 0% represents -100 dBm and 100% represents -50 dBm.


Answer for Question 6:
Standard deviation checks how spread out the data is in relation to the average. It is useful to calculate it because it tells us that the data is more dispersed if the standard deviation is higher.


Answer for Question 7:
A data frame is a 2-dimensional, data container that has column labels for each piece of data beneath it. For this case, the data frame iterates through every index of the data list that we have, and creates a new row after every third index. This is because of how we created three column labels when creating this data frame.


Answer for Question 8:
Error bars are important because it tells us about the reliability of the data collected. They tell us that there is higher uncertainty if the error bar is bigger.


Answer for Question 9:
Although the signal strength is similar for all locations, there exists a slight difference. Since the values of signal strength are negative, I was able to find the location with better signal by finding the shorter bar in the graph. Signal strength might be weaker in certain locations because there are more obstacles such as many layers of wall that disturbs the path of the signal.


Answer for Question 10:
For the resulting data it seems clear that the signals are very similar to each other since the signals given experience a delay that's usually around 3 ms. I do find it interesting that the delay decreases as the message size increases to 1000 bytes, but I know if I can perfectly explain why this is the case. It might have to do with the bandwidth of the signal between server and client being around 1000 bytes.

...
