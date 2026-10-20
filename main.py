"""name=input("Enter your name: ")
while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}")
food = input("Enter your favorite food: ")
while not food == "a":
    print(f"tasty {food}")
    food = input("Enter your favorite food: ")
print("bye ")"""
age = int(input("Enter your age: "))
while age < 1 or age > 10:
    print(f"{age} is invalid ")
    age = int(input("Enter your age: "))
print(f"Your age is {age}")