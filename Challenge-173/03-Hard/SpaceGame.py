from random import randint
from time import sleep

def slow_print(text):
	for letter in text + '\n':
		print(letter, end='', flush=True)
		sleep(0.03)

def choice(options_text, options_numbers):
	response = ''
	for option in options_text:
		print(option)
	response = input('Enter your choice: ')
	while response not in options_numbers:
		print('\nInvalid answer!!')
		response = input('Enter your choice: ')
	return response


slow_print("""

It is 2114. We have colonized the Galaxy.
To communicate we send 140 character max messages using [A-Z0-9].
The technology to do this requires faster than light pulses to beam the messages to relay stations.

Your job is to travel to another planet in your system and implement the Intergalactic Bitstreaming machine.

That planet is 1% of a lightyear away.

All you have is a broken spaceship, 300 food and 400 oxygen.

Your mission is to get to the other planet as quickly as possible. To do so, you'll have to pick up people along the way. These people will have different skills - it's up to you to decide who you want aboard your ship!
""")

#Inventory
broken_spaceships = 1
food = 300
oxygen = 400
food_savings_factor = 1 #No savings

#Travel stats
speed = 2280 #km per day
acceleration_factor = 1
distance = 9.5e12/100

#Progress and resources.
traveled = 0
day = 0
oxygen_per_day = 10
food_per_day = 10

#Crew
engineers = 0
chefs = 0
farmers = 0

first_names = ['Youlanda', 'Tu', 'Jerry', 'Xuan', 'Dessie', 'Demetrius', 'Melaine', 'Natacha', 'Boyce', 'Vannessa']
last_names = ['Ackerman', 'Saucedo', 'Yarbrough', 'Cleveland', 'Kahn', 'Oswald', 'Staley', 'Bowden', 'Adcock', 'Hooks'] #http://random-name-generator.info/random/?n=10&g=1&st=3
jobs = ['Engineer', 'Chef', 'Farmer']

while traveled<distance:
  sleep(3)
  day = day + 1
  print("#############################################################")
  slow_print("Day " + str(day) + ", Year 2114.")
  #Will we find someone today?
  if randint(0,10) > 1: #90% chance of finding someone.
    slow_print('You found someone along the way!')
    first_name = first_names[randint(0,9)]
    last_name = last_names[randint(0,9)]
    job = jobs[randint(0,2)]
    slow_print("It's " + first_name + " " + last_name + " (" + job + ")")
    slow_print("Would you like to have " + first_name + " " + last_name + " join the crew?")
    if job=="Engineer":
      print("""
        Abilities: 
        * Will repair something in the spaceship and triple your speed every day.
        * Eats 15 food
        * Uses 10 oxygen
        """)
    elif job=="Chef":
      print("""
        Abilities: 
        * Will prevent food waste: -20% food consumption
        * Eats 20 food
        * Uses 15 oxygen
        """)
    elif job=="Farmer":
      print("""
        Abilities: 
        * Will produce 25 food and 15 oxygen every day.
        * Eats 10 food
        * Uses 10 oxygen
        """)
    crew_choice = choice(["1. Yes", "2. No"], ["1", "2"])
    if crew_choice=="1":
      if job=="Engineer":
        engineers = engineers + 1
        acceleration_factor = acceleration_factor*2
        food_per_day = food_per_day + 15
        oxygen_per_day = oxygen_per_day + 10
      elif job=="Chef":
        chefs = chefs + 1
        food_per_day = food_per_day + 20
        oxygen_per_day = oxygen_per_day + 15
        food_savings_factor = food_savings_factor*1.2
      elif job=="Farmer":
        farmers = farmers + 1
        food_per_day = food_per_day - 15
        oxygen_per_day = oxygen_per_day - 5
  else:
    slow_print("You didn't find anyone today.\n\n")

  food = food - food_per_day/food_savings_factor
  oxygen = oxygen - oxygen_per_day
  speed = speed*acceleration_factor
  traveled = traveled + speed


  slow_print("CREW: \n Farmers: " + str(farmers) + "\n Chefs: " + str(chefs) + "\n Engineers: " + str(engineers))
  slow_print("\nRESOURCES: \n Food: " + str(food) + "\n Oxygen:" +  str(oxygen))
  slow_print(" Progress: " +  str(traveled/distance*100) + "%")
  slow_print(" Speed: " + str(speed) + " km per day")
  if food <= 0 or oxygen <= 0:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGAME OVER\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    score = round(traveled/1000000000 + food + oxygen + (15-days)*10)
    slow_print("Score: " + str(score))
    break
if traveled>distance:
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYOU WIN!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  score = round(traveled/1000000000 + food + oxygen)
  slow_print("Score: " + str(score))
