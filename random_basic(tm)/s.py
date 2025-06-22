import time
duration = input("Please set the timer (minutes-seconds) " )
minutes_over = False
minutes = "0"
seconds = "0"
for x in duration: 
    if x != "-" and minutes_over == False:
        
        minutes = minutes + x
        
    if minutes_over == True:
        seconds = seconds +  x
        
    if x == "-":
        minutes_over = True
minutes = int(minutes)      
seconds = int(seconds)
while True:
    confirmation = input(f"Do you want to set the timer to {minutes} minutes and {seconds} secodns? (y/n) ")
    if confirmation == "y":
        
        ttime= minutes * 60  + seconds
        time.sleep(ttime)
        print("done")
        break
    if confirmation =="n": 
        break
