import time
t=(time.strftime('%H:%M:%S'))
hour= int(time.strftime('%H'))
print("Current time in hours in India is:",hour)
if(hour>=12 and hour<=15):
    print("Good Afternoon!")
elif (hour>=4 and hour<=12):
    print("Good Morning!")
elif(hour>15 and hour<20):
    print("Good Evening!")
else:
    print("Good Night!")
