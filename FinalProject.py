import os
# created the file gamerating.txt
f1 =  open("GameRating.txt", "a")
#checks the input of the rating so its between 1-5
def checkIfWithinRange(rating):
  if rating not in range(1,6):
    print("\nRating must be within 1-5! Try again.\n")
    return 0
  return 1

# Populates the games dictionary with games and rating from the file.
def populateGamesDict(gamesDict):
  f1 = open("GameRating.txt", "r")
  for line in f1:
      line = line.split('::')
      game = line[0]
      rating = line[1]
      gamesDict[game] = rating
  f1.close()
# Populates the hours dictionary with games and rating from the file.
def populateHoursDict(gameHours):
    f1 = open("GameRating.txt", "r")
    for line in f1:
        line = line.split('::')
        game = line[0]
        hours = line[2]
        gameHours[game] = hours.rstrip("\n")
    f1.close()
#sorts the list of the items and adds a bullet in the beginning of each item.
def printSortedListItems(list):
  list.sort()
  for item in list:
    print(" • " + item)
#the dictionary for the games and the hours of the games.
games = {}
gameHours = {}
option = ""

# Source: https://www.tutorialspoint.com/python/os_stat.htm
# Checking to see if 'GameRating.txt' is empty
if(os.stat("GameRating.txt").st_size > 0):
  populateGamesDict(games)
  populateHoursDict(gameHours)
#prints the title of the program
print("----------------------------")
print("Game Rating and Hour Tracker")
print("----------------------------")
#runs a loop of the options until you select the exit option.
while(option != "e"):
#prints the menu and the options.
  print("\nMenu:")
  print("a) Add Game\nb) Sort Games By Rating\nc) Sort Games By Specified Hours\ne) Exit program\n")
#input the option from the menu.
  option = input("Enter an option: ")
  print("\n")
#if option a input the name of the game,rating and hours.
  if option == "a":
      while True:
          f1 = open("GameRating.txt", "a")
          game = input("Enter Game title or 'x' to exit: ")
#if input 'x' ends the loop and goes back to the menu.
          if(game == "x"):
            print("\n")
            break;
#checks the range to make sure its true else it prints an error.
          isInRange = 0
          while(isInRange == 0):
            rating = int(input("Enter a rating from 1-5: "))
            isInRange = checkIfWithinRange(rating)
#input hours of the amount spent on the game.
          hours = int(input('Enter number of hours played: '))
# adds the game,rating, and hours into the game dictionary.
          gameRating = (game + '::' + str(rating) + '::' + str(hours))
          games[game] = rating
          f1.write(gameRating + "\n")
          f1.close()
      f1.close()
#if b is selected, sort list by the rating.
  elif option ==  "b":
      f1 = open("GameRating.txt", 'r')
      gameList = []
      userRating = int(input("Enter a rating between 1-5: "))

      for key, value in games.items():
        if(int(value) == int(userRating)):
          gameList.append(key)
#prints games in sorted order.
      printSortedListItems(gameList)
#if option c is selected. The list displays by the input of hours.
  elif option == "c":
      f1 = open("GameRating.txt", 'r')
      hoursList = []
      gameHourPair = dict()
#Test the input for errors and handle by going to the menu.
      try:
        hours = int(input("Enter hours: "))
      except:
        print("Input must me a number")
        continue
#the key is game, the value is the hours
      for key, value in gameHours.items():
        if(int(value) <= int(hours)):
          gameHourPair[key] = value;
      for key, value in gameHourPair.items():
        print(" • " + key + " - played for " + value + " hours")
#the code ends when 'e' is inputted.
  elif option == "e":
    print("\nExiting ...\n")
    exit()
  else:
    print("\nInvalid option! Try again.\n")
