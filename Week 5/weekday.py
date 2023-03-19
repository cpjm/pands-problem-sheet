# Script: weekday.py
# author: Ciaran Moran
# 
# This script will check the weekday for teh current day.
# It will then display some "joy" on the screen if it's teh weekend.
# However if a weekday then display some dismay!
#
# This is version 1 using a list 
#
# Source:
# For this code I used the following website
# https://pynative.com/python-get-the-day-of-week
# There are several solutions given. I went with the first one
# as this was intuative enough for me. However each solution was similar in nature.
#

# import the phtyon system date time functions
from datetime import date
import calendar
weekend_days = ['Saturday','Sunday']
curr_date = date.today()
curr_day_text = calendar.day_name[curr_date.weekday()]
print ((curr_date,curr_date), curr_day_text)
if curr_day_text in weekend_days:
    print ("It is the weekend, yay!") 
else :
    print ("Yes, unfortunately today is a weekday.")
