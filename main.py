import calendar
import random
import os 
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Game:
    def __init__(self):
        self.miles = 2000
        self.food = 500
        self.health = 5
        self.year = 2020
        self.month = 12
        self.day = 25 
        self.active = True
        self.num_days = self.get_days(self.year , self.month)
        self.weekdict =  {0: "Monday", 1:"Tuesday" , 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        self.bad_things = ["You get COVID-19", "River","Your Car Wagon Broke Down", "Your partner dumped you","You realize you suck" , "You go to school", "Your friends are awful people", "You Havent died yet", "You get wet socks"]
        self.bad_things_index = {}
    def get_days(self, year , month):
        num_days = []
        cal = calendar.Calendar() 
        for i in cal.itermonthdays(year , month):
            num_days.append(i)

        return max(num_days)
    def create_events(self):
        for i in range(1, 13):
            ran = random.randint(1 , self.get_days(self.year , i))
            self.bad_things_index[i] = [ran , random.choice(self.bad_things)]
        print(self.bad_things_index)
    def end_turn(self):

        if (self.day >= self.bad_things_index[self.month][0]):
            print(self.bad_things_index[self.month][1])
            bad_thing = random.randint(2, 5)
            self.handle_time_change(bad_thing)
            self.food -= bad_thing * 4
            self.health -= bad_thing

        if (random.randint(0, 5) == 3):
            self.health -= 1
            print("You got ganked")
        if (self.food <= 0 or self.health <= 0):
            cls()
            print("You die in a very sad pathetic way")
            self.active = False
            quit()
        elif (self.miles <= 0):
            cls()
            print("You Won!!!")
            self.active = False
            quit()
        time.sleep(3)
        cls()
    def handle_time_change(self, time_used):
        if (self.day + time_used > self.num_days):
            if (self.month < 12):
                self.month += 1
                self.day = (self.day + time_used) - self.num_days
                self.num_days = self.get_days(self.year , self.month)
            else:
                cls()
                print("You died, You were to slow")
                self.active = False
                quit()
        else:
            self.day += time_used

class Player(Game):
    def __init__(self):
        Game.__init__(self)
  
    def travel(self):
        travel_distance = random.randint(30, 60)
        self.miles -= travel_distance 
        travel_time = random.randint(3, 7)
        self.handle_time_change(travel_time)  
        self.food -= travel_time * 5


    def rest(self):
        rest_days = random.randint(2, 5)
        health_add = random.randint(1, 5)
        self.health += health_add
        self.handle_time_change(rest_days)
        self.food -= rest_days *2

    def hunt(self):
        self.food += 100
        food_days = random.randint(2, 5)
        self.handle_time_change(food_days)
        self.food -= food_days * 4

    def status(self):
        print("food: ", self.food , " health: ", self.health, " miles left: ", self.miles)
        print("date: ", calendar.month_name[self.month], self.weekdict[calendar.weekday(self.year, self.month , self.day)],self.day , self.year)

    def action(self):
        self.status()
        print("\n 1: travel \n 2: hunt \n 3: rest")
        try:
            choice = int(input(": "))
            if (choice == 1):
                self.travel()
            if (choice == 2):
                self.hunt()
            if (choice == 3):
                self.rest()
        except:
            print("That action is invaild")
            time.sleep(1)
            cls()
        #actions[choice]

player = Player()
player.create_events()
#while player.active:
#    player.action()
#    player.end_turn()