current_movies = {"The Avengers": "12:00pm",
"The Arrival": "6:00pm",
"Scary Movie": "11:00am",
"Bob's Burger": "5:00pm"}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input("what movie showtime would you like?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie is not playing")
else:
    print(movie, "is playing at", showtime)