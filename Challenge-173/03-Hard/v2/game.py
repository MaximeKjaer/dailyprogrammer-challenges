from random import randint
from time import sleep
import json

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


with open('game.json') as f:
  game = json.load(f)


slow_print(game['initial_text'])

while game['stats']['traveled'] < game['stats']['distance']:
  sleep(3)
  game['stats']['day'] += 1
  print("#############################################################")
  slow_print("Day " + str(game['stats']['day']) + ", Year 2114.")
  #Will we find someone today?
  if randint(0,10) > 1: #90% chance of finding someone.
    slow_print('You found someone along the way!')
    #Randomly chosing a few things
    first_name = game['first_names'][randint(0, len(game['first_names'])-1)]
    last_name = game['last_names'][randint(0, len(game['last_names'])-1)]
    job = game['jobs'][randint(0, len(game['jobs'])-1)]
    #Printing what we've chosen
    slow_print("It's " + first_name + " " + last_name + " (" + job + ")")
    slow_print("Would you like to have " + first_name + " " + last_name + " join the crew?")
    print('\n' + game['job_stats'][job]['text'])
    #Should they come aboard?
    crew_choice = choice(["1. Yes", "2. No"], ["1", "2"])
    if crew_choice=="1":
      #How does the new crew member affect the ship's stats?
      game['stats'][job.lower() + 's'] += 1
      game['stats']['acceleration_factor'] *= game['job_stats'][job]['acceleration_factor']
      game['stats']['food_savings_factor'] *= game['job_stats'][job]['food_savings_factor']
      game['stats']['oxygen_savings_factor'] *= game['job_stats'][job]['oxygen_savings_factor']
      game['stats']['food_per_day'] += game['job_stats'][job]['food']
      game['stats']['oxygen_per_day'] += game['job_stats'][job]['oxygen']
  else:
    slow_print("You didn't find anyone today.\n\n")
  #What has been used/done today
  game['stats']['food'] -= round(game['stats']['food_per_day'] / game['stats']['food_savings_factor'])
  game['stats']['oxygen'] -= game['stats']['oxygen_per_day']
  game['stats']['speed'] *= game['stats']['acceleration_factor']
  game['stats']['traveled'] += game['stats']['speed']


  slow_print('CREW:')
  for job in game['jobs']:
    slow_print(' ' + job + 's: ' +  str(game['stats'][job.lower() + 's']))

  slow_print("\nRESOURCES: \n Food: " + str(game['stats']['food']) + "\n Oxygen: " +  str(game['stats']['oxygen']))
  slow_print(" Progress: " +  str( (game['stats']['traveled'] / game['stats']['distance']) *100) + '%')
  slow_print(" Speed: " + str(game['stats']['speed']) + " km per day")
  if game['stats']['food'] <= 0 or game['stats']['oxygen'] <= 0:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGAME OVER\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    score = round(game['stats']['traveled']/1000000000 + game['stats']['food'] + game['stats']['oxygen'] + (15-game['stats']['day'])*10)
    slow_print("Score: " + str(score))
    break
if game['stats']['traveled'] > game['stats']['distance']:
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYOU WIN!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  score = round(game['stats']['traveled']/1000000000 + game['stats']['food'] + game['stats']['oxygen'] + (15-game['stats']['day'])*10)
  slow_print("Score: " + str(score))
