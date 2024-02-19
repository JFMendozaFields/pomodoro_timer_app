import time
import datetime

class Timer:
    def __int__(self, h, m, s):
        self.h = h 
        self.m = m 
        self.s = s 
        
    
    def countdown(self, h, m, s):
        total_seconds = h * 3600 + m * 60 + s

        while total_seconds > 0:

            timer = datetime.timedelta(seconds = total_seconds)

            print(timer, end="r")

            time.sleep(1)
        
            total_seconds -= 1
        print("Bzzt!! Timer is done!")

    

def time_input():
    h = input("Please enter hours: ")
    m = input("Please enter minutes: ")
    s = input("Please enter seconds: ")
    countdown = Timer()
    countdown.countdown(int(h), int(m), int(s))
time_input()
