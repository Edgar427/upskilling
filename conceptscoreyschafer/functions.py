def hello_func(greeting, name = "You"):
    return(f"{greeting}, {name}")

print(hello_func( name = "John", greeting= "Hi"))


# packing and Unpacking
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]

info = {"Name" : "John", "age" : 22}

student_info(*courses, **info)