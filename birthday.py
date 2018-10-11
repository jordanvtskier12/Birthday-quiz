"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name=str(input("Hello, what is your name? "))
month=str(input("Hi "+name+", what was the name of the month you were born in? "))
year=int(input("And what year were you born in, "+name+"? "))
day=int(input("And the day? "))

months = ["" , "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ""]


winter=['December','January','February']
spring=['March','May','April']
summer=['June','July','August']
fall=['September','October','November']

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day


birthmonth = months[todaymonth]
if month=="October" and day==31:
    print("You were born on Halloween!")
    
    
elif month==birthmonth and day==todaydate:
    print("Happy birthday!")



elif month in [winter] and year>=2000:
    print(str(name + ", you are a winter baby of the two thousands."))
elif month in [spring] and year>=2000: 
    print(str(name + ", you are a spring baby of the two thousands."))
elif month in [summer] and year>=2000:
    print(str(name +", you are a summer baby of the two thousands."))
elif month in [fall]  and d>=2000:
    print(str(name + ", you are a fall baby of the two thousands."))
    
    
elif month in [winter] and year>=1990 and year<= 2000:
    print(str(name + ", you are a winter baby of the nineties."))
elif month in [spring] and year>=1990 and year<= 2000:
    print(str(name + ", you are a spring baby of the nineties."))
elif month in [summer] and d>=1990 and d<=2000:
    print(str(name + ", you are a summer baby of the nineties."))
elif month in [fall]  and year>=1990 and year<=2000:
    print(str(name + ", you are a fall baby of the nineties."))
    
    
elif month in [winter] and year>=1980 and year<= 1990:
    print(str(name + ", you are a winter baby of the eighties."))
elif month in [spring] and year>=1980 and year<= 1990:
    print(str(name + ", you are a spring baby of the eighties."))
elif month in [summer] and year>=1980 and year<=1990:
    print(str(name + ", you are a summer baby of the eighties."))    
elif month in [fall]  and year>=1980 and year<=1990:
    print(str(name + ", you are a fall baby of the eighties."))
    
    
elif month in [winter]  and year<=1980:
    print(str(name + ", you are a winter baby of the Stone Age."))
elif month in [spring] and year<=1980: 
    print(str(name + ", you are a spring baby of the Stone Age."))
elif month in [summer] and year<=1980:
    print(str(name +", you are a summer baby of the Stone Age."))
elif month in [fall] and year<=1980:
    print(str(name + ", you are a fall baby of the Stone Age."))
    
    
    