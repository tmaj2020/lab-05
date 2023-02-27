import platform
import time
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import re

def get_wifi_signal_strength() -> int:
    """Get the signal strength of the wifi connection.
    
    Returns:
        The signal strength in dBm.
    """
    # Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
    # dBm is decibel-milliwatts, a unit used to measure power. Signal strength is proportional to link
    # speed, which means that higher values are considered better.

    # Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
    # We need to check the OS since each OS may have different methods or commands that need
    # to be called to check the signal level. The difference between these commands appear to mainly
    # be syntax based, but they also appear to have different names for the signal level since Linux
    # has it listed as “Signal level=(-?\d+) dBm”, Windows has it as “Signal\s*:\s*(\d+)%” and
    # Mac has it listed as “agrCtlRSSI:\s*(-?\d+)”

    # Question 3: In your own words, what is subprocess.check_output doing? What does it return?
    # HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output
    # Subprocess.check_output() appears to be running a command within the shell of the computer
    # running this program and returns the output of that command in the form of a utf-8 encoded
    # object

    # Question 4: In your own words, what is re.search doing? What does it return?
    # HINT: https://docs.python.org/3/library/re.html#re.search
    # Re.search appears to look through the output object that was received from
    # subprocess.check_output, and is looking for a specific line of information from that object after it
    # is decoded from utf-8. This command should return the matching object and none if there isn’t a
    # match found.

    # Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
    # HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
    # We need to convert the signal quality not necessarily to dBm, but to the actual RSSI signal in
    # dBm. This is because of how the signal is returned as percentage, where 0% represents -100
    # dBm and 100% represents -50 dBm.

    if platform.system() == 'Linux': # Linux
        output = subprocess.check_output("iwconfig wlan0", shell=True)
        match = re.search(r"Signal level=(-?\d+) dBm", output.decode('utf-8'))
        signal_strength = int(match.group(1))
    elif platform.system() == 'Windows': # Windows
        output = subprocess.check_output("netsh wlan show interfaces", shell=True)
        match = re.search(r"Signal\s*:\s*(\d+)%", output.decode('utf-8'))
        signal_quality = int(match.group(1))
        signal_strength = -100 + signal_quality / 2
    elif platform.system() == 'Darwin': # Mac
        output = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True)
        match = re.search(r"agrCtlRSSI:\s*(-?\d+)", output.decode('utf-8'))
        signal_strength = int(match.group(1))
    else:
        raise Exception("Unknown OS")

    return signal_strength

def main():
    # Choose at least 5 locations to sample the signal strength at
    # These can be rooms in your house, hallways, different floors, outside, etc. (as long as you can get a WiFi signal)
    locations = ['bedroom', 'living room', 'kitchen', 'bathroom', 'garage']
    samples_per_location = 10 # number of samples to take per location
    time_between_samples = 1 # time between samples (in seconds)

    data = [] # list of data points
    for location in locations:
        print(f"Go to the {location} and press enter to start sampling")
        input() # wait for the user to press enter
        signal_strengths = [] # list of signal strengths at this location
        signal_strengths.clear()

        # TODO: collect 10 samples of the signal strength at this location, waiting 1 second between each sample
        # HINT: use the get_wifi_signal_strength function
        for i in range(samples_per_location):
            dBm = get_wifi_signal_strength()
            signal_strengths.append(dBm)
            time.sleep(time_between_samples)    
            
        
        
        # TODO: calculate the mean and standard deviation of the signal strengths you collected at this location
        signal_strength_mean = np.mean(signal_strengths)
        signal_strength_std = np.std(signal_strengths)

        # Question 6: What is the standard deviation? Why is it useful to calculate it?
        # standard deviation checks how spread out the data is in relation to the average. It is useful to 
        # calculate it because it tells us that the data is more dispersed if the standard deviation is higher.
        data.append((location, signal_strength_mean, signal_strength_std))

    # create a dataframe from the data
    df = pd.DataFrame(data, columns=['location', 'signal_strength_mean', 'signal_strength_std'])

    # Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
    # HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    # HINT: print the dataframe to see what it looks like
    # A data frame is a 2-dimensional, data container that has column labels for each piece of data beneath it. 
    # For this case, the data frame iterates through every index of the data list that we have, and creates a new 
    # row after every third index. This is because of how we created three column labels when creating this data 
    # frame.

    print(df)

    # TODO: plot the data as a bar chart using plotly
    # HINT: https://plotly.com/python/bar-charts/
    # NOTE: use the error_y parameter of px.bar to plot the error bars (1 standard deviation)
    #   documentation: https://plotly.com/python-api-reference/generated/plotly.express.bar.html
    fig = px.bar(
        df, 
        x='location', 
        y='signal_strength_mean', 
        error_y ='signal_strength_std',
        title='Signal Strengths Per Location',
        labels={
            'location': 'Location',
            'signal_strength_mean': 'Average Signal Strength (dBm)',
        },


        template='plotly_white'
        
    )
    # Question 8: Why is it important to plot the error bars? What do they tell us?
    # Error bars are important because it tells us about the reliability of the data 
    # collected. They tell us that there is higher uncertainty if the error bar is bigger.



    # write the plot to a file - make sure to commit the PNG file to your repository along with your code
    fig.write_image("signal_strength.png")

    # Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
    #             Why do you think signal strength is weaker in certain locations?
    # Although the signal strength is similar for all locations, there exists a slight difference. Since the 
    # values of signal strength are negative, I was able to find the location with better signal by finding the 
    # shorter bar in the graph. Signal strength might be weaker in certain locations because there are more 
    # obstacles such as many layers of wall that disturbs the path of the signal.


if __name__ == "__main__":
    main()