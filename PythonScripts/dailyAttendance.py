# A40
# Daily Attendance

import pandas as pd
import matplotlib.pyplot as plt

file = input('Enter name of input file: ')          # dailyAttendanceManHunt2018.csv
output = input('Enter name of output file: ')       # dailyAttendanceManHunt2018.png

attn = pd.read_csv(file)

# Convert the 'Date' column to datetime format
attn["Date"] = pd.to_datetime(attn["Date"].apply(str))

# Calculate the percentage of students attending each session
attn['% Attending'] = attn['Present'] / attn['Enrolled'] * 100

# Plot the percentage of students attending over time
attn.plot(x="Date", y="% Attending")

# Get the current figure (plot) and save it to the specified output file
fig = plt.gcf()
fig.savefig(output)