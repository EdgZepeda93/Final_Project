import os

f1 =  open("GameRating.txt", "a")

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

def populateHoursDict(gameHours):
    f1 = open("GameRating.txt", "r")
    for line in f1:
        line = line.split('::')
        game = line[0]
        hours = line[2]
        gameHours[game] = hours.rstrip("\n")
    f1.close()

def printSortedListItems(list):
  list.sort()
  for item in list:
    print(" • " + item)

games = {}
gameHours = {}
option = ""

# Source: https://www.tutorialspoint.com/python/os_stat.htm
# Checking to see if 'GameRating.txt' is empty
if(os.stat("GameRating.txt").st_size > 0):
  populateGamesDict(games)
  populateHoursDict(gameHours)

print("----------------------------")
print("Game Rating and Hour Tracker")
print("----------------------------")

while(option != "e"):

  print("\nMenu:")
  print("a) Add Game\nb) Sort Games By Rating\nc) Sort Games By Specified Hours\ne) Exit program\n")

  option = input("Enter an option: ")
  print("\n")

  if option == "a":
      while True:
          f1 = open("GameRating.txt", "a")
          game = input("Enter Game title or 'x' to exit: ")

          if(game == "x"):
            print("\n")
            break;

          isInRange = 0
          while(isInRange == 0):
            rating = int(input("Enter a rating from 1-5: "))
            isInRange = checkIfWithinRange(rating)

          hours = int(input('Enter number of hours played: '))
          gameRating = (game + '::' + str(rating) + '::' + str(hours))
          games[game] = rating
          f1.write(gameRating + "\n")
          f1.close()
      f1.close()

  elif option ==  "b":
      f1 = open("GameRating.txt", 'r')
      gameList = []
      userRating = int(input("Enter a rating between 1-5: "))

      for key, value in games.items():
        if(int(value) == int(userRating)):
          gameList.append(key)

      printSortedListItems(gameList)

  elif option == "c":
      f1 = open("GameRating.txt", 'r')
      hoursList = []
      hours = int(input("Enter hours: "))

      for key, value in gameHours.items():
        if(int(value) <= int(hours)):
          hoursList.append(key)

      printSortedListItems(hoursList)

  elif option == "e":
    print("\nExiting ...\n")
    exit()
  else:
    print("\nInvalid option! Try again.\n")
