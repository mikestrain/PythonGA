from pytime import pytime
import os
os.system("clear")

def choose_holiday(year, holiday):
    
    list_of_holidays = ["christmas eve", "easter", "valentine's day"]

    if holiday.lower() in list_of_holidays:
        
        if holiday.lower() == list_of_holidays[0]:
            day = pytime.christeve(year)
        
        elif holiday.lower() == list_of_holidays[1]:
            day = pytime.easter(year)
        
        elif holiday.lower() == list_of_holidays[2]:
            day = pytime.valentine(year)
        
        return day

    else: print("sorry, that holiday is unknown.")

u_year = input("Please choose a year:")
u_holiday = input("Please choose a holiday:")

u_day = choose_holiday(year=u_year,holiday=u_holiday)

print(u_holiday,"is",u_day)