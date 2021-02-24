""" https://repl.it/@ps9610/Day-Two-Blueprint#main.py """
"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(day_list=[], day=""): #day_list=[]가 days를, day=""가 "Wed"를 받아주는 매개변수
  return day in day_list
  #day를 return해라, day_list안에 있는

def get_x(day_list=[], idx=0): #day_list=[]가 days를, idx=0이 3을 받아주는 매개변수
    return day_list[idx]
    #day_list 안에 있는 idx번호를 return해라

def add_x(day_list=[], days=""): #day_list=[]가 days를, day=""가 "Sat"을 받아주는 매개변수
  day_list.append(days)
  #

def remove_x(day_list=[], days=""): #day_list=[]가 days를, day=""가 "Mon"을 받아주는 매개변수
  day_list.remove(days)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #