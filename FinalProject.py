def r(rating):
    if rating in range(1,6):
        print("correct")
    else:
        print()
        exit()

f1 =  open("GameRating.txt", "w")


games = {}

# while True:
  # display menu options
  # ask user for option
  # if input equals a -> ask to enter game and rating
  # if input equals b -> ask user for a rating and display games for that rating
  # if input equals e -> exit program
  # create a menu by using an if statement
  # take in user input
while True:
  f1 = open("GameRating.txt", "a")
  game = input("Please Enter Game title: ").capitalize()
  if(game == "-1"):
    break;
  rating = int(input("Enter rating from 1-5: "))
  gameRating = (game + '::' + str(rating))
  r(rating)
  games[game] = rating
  f1.write(gameRating + '\n')
  f1.close()


print(games)
f1.close()
# games[key] = value -> game is the key, rating is the value

#ratingTest = int(input("Enter rating from 1-5: "))

ratedGamesList = []
userRating = int(input("Enter a rating you want to output games for:"))

for key, value in games.items():
  if(value == userRating):
    ratedGamesList.append(key)

print(ratedGamesList)

#add hours
#display games in alphabetical order sorting
