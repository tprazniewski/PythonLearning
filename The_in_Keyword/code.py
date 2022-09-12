# friends = ["Tom", "Fab"]

# print("Tom" in friends)

movies = ["The Matrix", "Green Book"]

user_movie = input("Enter somthing you've watcher recently:")

if user_movie in movies:
    print(f"I have also watcher {user_movie}")
else:
    print("i haven't watchet that yet")