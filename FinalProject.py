import os

f1 =  open("GameRating.txt", "a")

def r(rating):
    if rating in range(1,6):
        print()
    else:
        print()
        exit()
def s(gameRating):
    for line in f1:
        line = line.split('::')
        ratedGameList = line[0]
        rate = line[1]
        gameRate = (ratedGameList + '::' + rate)
        print(gameRate)
    f1.close()

# Populates the games dictionary with games and rating from the file.
def populateGamesDict(gamesDict):
  f1 = open("GameRating.txt", "r")
  for line in f1:
      line = line.split('::')
      game = line[0]
      rating = line[1]
      gamesDict[game] = rating
  f1.close()


games = {}
if(os.stat("GameRating.txt").st_size > 0):
  populateGamesDict(games)

print(games);
option = input("Enter 1 to add game, Enter 2 to sort by rating, Enter 3 for hours played: ")
if option == "1":
    while True:
        f1 = open("GameRating.txt", "a")
        game = input("Please Enter Game title or 'E' to exit: ").capitalize()
        if(game == "E"):
            break;
        rating = int(input("Enter rating from 1-5: "))
        hours = int(input('Enter number of hours played: '))
        gameRating = (game + '::' + str(rating) + '::' + str(hours))
        r(rating)
        games[game] = rating
        f1.write(gameRating + '\n')
        f1.close()
    print(games)
    f1.close()

elif option == '2':
    f1 = open("GameRating.txt", 'r')
    gameList = []
    userRating = int(input("Enter a rating you want to output games for:"))
    for key, value in games.items():
      if(int(value) == int(userRating)):
        gameList.append(key)
    gameList.sort()
    for game in gameList:
      print(game)

elif option == '3':
    f1 = open("GameRating.txt", 'r')
    hours = dict()
    for line in f1:
        line = line.split('::')
        hours = line[1]
        print(hours)
    f1.close()
else:
    exit()
#add hours
#display games in alphabetical order sorting
# while True:
# display menu options
# ask user for option
# if input equals a -> ask to enter game and rating
# if input equals b -> ask user for a rating and display games for that rating
# if input equals e -> exit program
# create a menu by using an if statement
# take in user input
