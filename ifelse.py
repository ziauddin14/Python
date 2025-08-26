#Creating a good morning message based on the time of day
import time 
hour = int(time.strftime('%H'))  # صرف گھنٹے نکالیں

if (hour < 12):
    print("Good Morning!")
elif (hour >= 12 and hour < 17):  n
    print("Good Afternoon!")
else:
    print("Good Evening!")