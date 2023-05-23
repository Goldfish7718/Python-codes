import time

hour = int(time.strftime("%H"))

if (hour >= 00 and hour <= 12):
    print("Good Morning")
elif (hour > 12 and hour <= 18):
    print("Good Afternoon")
elif (hour > 18 and hour <= 21):
    print("Good Evening")
else:
    print("Good Night")
