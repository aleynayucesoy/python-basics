print(" --- Dict içinden veri okuma ---")

user = {
    "name" : "Aleyna",
    "age" : 27,
    "email" : "test@email.com",
    "skills" : ["JS", "React"]
}

print(user)

print("\n//////////////////\n")

print("Name: ", user["name"])
city = user.get("city", "not-found")
print("City: ", city)

print("\n//////////////////\n")
print(" --- Nested Dict ---")

users = {
    "user1" : {
        "username" : "aleyyo",
        "name" : "Aleyna",
        "email" : "test@email.com",
        "admin" : True
    },
    "user2" : {
        "username" : "Yurdo",
        "name" : "Yurdaer",
        "email" : "test@email.com",
        "admin" : False
    },
}

print("Users: ")
print(users)