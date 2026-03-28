A = [1,2,3]

# Append - insert element to the end of a list - On average: O(1)
A.append(5)
print(A)

# Pop - Deleting an element at the end of list - O(1)
A.pop()

print(A)

#Insert (not at the end of list) - O(n)

A.insert(2, 5)

print(A)


#Modify an element - O(1)
A[0] = 7

print(A)

#Accessing element with a given index i - O(1)
print(A[2])


#Checking if array has an element - O(n)
if 7 in A:
    print(True)


#Checking length - O(1)
print(len(A))

#Strings

#Append to end of string - O(n)

s = "Hello"
b = s + "z"

print(b)

#check if something is in string - O(n)
if "f" in s:
    print(True)

#Access positions - O(1)

print(s[2])

#Checking length - O(1)
print(len(s))