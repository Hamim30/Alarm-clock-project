from datetime import datetime #Tp get the actual time
from playsound import playsound #To Alarm tune
alarm_time = input("Alarm time hour:minute:second:AM/PM\n")  #Alarm set in this format hour:minuite:second:period(AM/PM)
#Note: If you want to set alarm which is less than 10 like 9:40:00:pm please type 09:40:00:pm
alarm_hour    = alarm_time[0:2]  #0 to 2 index is basically hour
alarm_minute  = alarm_time[3:5]  #3 to 5 is basically minuite
alarm_seconds = alarm_time[6:8]  #6 to 8 is basically second
alarm_period  =  alarm_time[9:11].upper()  #9 to 11 is basically period.to avoid It's Case sensitivity I use upper
print("Done") #just to know code is working till now
while True:
    now = datetime.now()  #Import the datetime module and display the current date/time
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    #From line 12 to 15, continuously checking the time with the help of DateTime module %I, %M actually returning me the current time. DateTime module also has other features like a month, year. we do not need those now
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
    #from line 17 to 20 I am continously checking my hour , minute, second , period is matching with current time or not .
                    print("Alamr bajibo ekhon :3")
                    playsound('alarm-alarm.mp3') #if every conditions remain TRUE playsound module will play the alarm-alarm.mp3
                    break
    #NOTE: pleasae make sure your alarm-alarm file and your py file in the same folder.otherwise you have give the path to find the file



