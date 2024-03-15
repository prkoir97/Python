# A17
# Time Remaining

print("Time Remaining Until Lecture!")

seconds = float(input('Enter Number of Seconds: '))

hours = seconds //3600
rem = seconds % 3600
minutes = rem //60
remSec = rem % 60

print("Hours: ",hours)
print("Minutes: ",minutes)
print("Seconds: ",remSec)
