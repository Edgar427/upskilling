name = input("Enter your name: ")
age = input("Enter your age: ")

message = f"Hello {name}, you are {age} y/o"
print(message)

#with open("input.txt", "r") as f:
#    input_data = f.read()

with open("output.txt", "w") as f:
    f.write(message)
