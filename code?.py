import calendar
import random
import os
import time 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

w = 25
m = 3
randomls = []
mons = ["January","February","March","April","May","June","July","August","September","October","November","December"]

bad_stuff = ["you get COVID-19", "you drink piss" , "you step on dog shit"," you get cancer","river","your car wagon","your girlfriend dumped you", "you realize you suck"]

calmonth = calendar.month_name[m]
cal = int(calendar.weekday(1836 , m , w ))
numday = w 
def current_weekday():
  global cal
  if cal == 0:
    cal = "Monday"
  if cal == 1:
    cal = "Tuesday"
  if cal == 2:
    cal = "Wednesday"
  if cal == 3:
    cal = "Thursday"
  if cal == 4:
    cal = "Friday"
  if cal == 5:
    cal = "Saturday"
  if cal == 6:
    cal = "Sunday"
current_weekday()
print(calmonth,cal,numday)


if calmonth == "February":
	num_days = 29
elif calmonth in ("April", "June", "September", "November"):
	num_days = 30
elif calmonth in ("January", "March", "May", "July", "August", "October", "December"):
	num_days = 31

miles = 2000
food = 500
health = 5
b = 0
def travel():
  global miles
  global food
  global w
  global m
  global b
  travel_distance = random.randint(30,60)
  miles -= travel_distance
  travel_time = random.randint(3,7)
  w += travel_time
  if w > num_days:
    remainder = w - num_days 
    b += 1
    m += 1
    w = 0
    w += remainder
    
  food -= travel_time * 5 
  
def rest():
  global health
  global w
  global health_add
  global m
  global food
  global b 
  rest_days = random.randint(2,5)
  health_add = random.randint(1,5)
  health += health_add
  w += rest_days
  if w > num_days:
    remainder = w - num_days 
    b += 1
    m += 1
    w = 0
    w += remainder
  food -= rest_days * 2
  
    
def hunt():
  global food
  global w
  global m
  global b
  food += 100
  food_days = random.randint(2,5)
  w += food_days
  if w  > num_days:
    remainder = w - num_days 
    b += 1
    m += 1
    w = 0
    w += remainder
  food -= food_days * 4
  
name = input("what is your name?: ")

for x in mons:
 random_date = random.randint(1,num_days-5)
 randomls.append(random_date)
#print(randomls)

print(randomls)
game_acitve = True
while game_acitve == True:
  current_mon = mons[0 + b]
  for x in mons:
    if current_mon == x:
      index_1 = mons.index(current_mon)
      print(randomls[index_1])
      if w >= randomls[index_1]:
        print(random.choice(bad_stuff))
        bad_day = random.randint(2,5)
        w += bad_day
        if w  > num_days:
          remainder = w - num_days 
          b += 1
          m += 1
          w = 0
          w += remainder
        food -= bad_day * 4
        health -= bad_day 
        randomls[index_1] = 100
      choice = input("what do you want to do?: ")
      if choice == "travel":
        travel()
      if choice == "rest":
        rest()
      if choice == "hunt":
        hunt()
      if choice == "help":
        print("quit,hunt,rest,travel,status")
      if choice == "status":
        calmonth = calendar.month_name[m]
        cal = int(calendar.weekday(1836 , m , w ))
        numday = w 
        current_weekday()
        print("food: ",food, " health: ",health, " miles left: ",miles," date: ",calmonth,cal,numday)
      if choice == "quit":
        quit()
      if random.randint(0,5) == 3:
        health -= 1
        print('ye')
      if food <= 0 or health <= 0:
        #cls()
        print("you die 1")
        quit()
      if m >= 12 and w >= 31:
        cls()
        print("you die 2 ")
        quit()
      if miles <= 0:
        cls()
        print("you win 3")
        quit()
      time.sleep(3)
      cls()
