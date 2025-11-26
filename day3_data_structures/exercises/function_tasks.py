print(" --- *args ---")

def args_func(greeting, *names):
    for name in names:
        print(f"{greeting} {name}")
args_func("Selam", "Aleyna", "Mehmet", "Ali", "Veli")

print("\n--------------- \n")

def args_maxNumber(*numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
print(args_maxNumber(1,2,3,4,5,6,7,8,9,10))

print("\n//////////////////\n")
print(" --- **kwargs ---")

def kwargs_func(username, **details):
    print("Username: ", username)
    print("User infos: ")
    for key, values in details.items():
        print(" ", key + ": ", values)
kwargs_func("aleyyo", name = "Aleyna", age = 27, city = "Türkiye", hobby = "coding")