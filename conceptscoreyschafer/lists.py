courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]
nums = [1,5,4,3]
my_list = [0,1,2,3,4,5,6,7,8,9]
sample_url = "http://coreyms.com"
li = [9,1,8,2,7,3,6,4,5]
#print(len(courses)) to find length of list we use len()

#print(courses[0]) to see first element
#print(courses[-1]) to get last item of list can use course[3] as well

#Sliced list
# list[start:end:step] the end is noninclusive, up till the number but does not include the number
#print(courses[:-1]) history to physics
#print(courses[:2]) will print first 2 
#print(courses[2:]) will print from second element to the end
#print(courses[1:3]) will print second and third elements
#print(courses[:]) will get a copy of the entire list
#print(my_list[2:-1:2]) will print out every second value
#print(my_list[2:-1:-1]) will give an empty list because there is no way to go from 2 to 8 in reverse
#print(my_list[-1:2:-1]) will go in reverse from 9-3
#print(my_list[8:1:-2])
#print(my_list[::-1]) will give entire list in reverse

#Slicing a String
#print(sample_url[::-1]) reversing the url
#print(sample_url[-4:]) get the top level domain
#print(sample_url[7:]) #print the url without the http://
#print(sample_url[7:-4]) print the url without the http:// or the top level domain


#Adding to list
#courses.append("Art")
#courses.insert(0, "Art") Art was inserted at index 0
#courses.extend(courses_2) adds two lists, if done with others (Append/insert) will put a list inside a list

#Removing an element
#courses.remove("Math") will remove Math from list
#courses.pop() will remove last item (CompSci), can return value that it removes
#popped = courses.pop() returns compsci


#Sorting list
#courses.reverse() reverses list
#courses.sort() sorts in alphabetical order for strings or ascending order for numbers
#nums.sort()  ascending order for numbers
#courses.sort(reverse=True) decending order
#nums.sort(reverse=True) decending order
#num = sorted(nums, reverse = True) same as above
#print(num)


#List Functions
#sortedlist = sorted(courses) #sorted function, returns a sorted version of the list, can put in a variable
#useful because we don't want to alter original list
#print(min(nums)) returns the minimum value
#print(max(nums)) returns the max value
#print(sum(nums)) retuns the sum of all elements in list
#print(courses.index("CompSci")) will show index of element
#print("Math" in courses) to check if something is in list returns a boolean


#Looping through a list
#for index, course in enumerate(courses, start = 1): #to access index and value , start = 1 if we want to start from 1 History instead of 0 History
#    print(index, course)


#List to Strings, example list of courses into a comma separated values
#course_String = " - ".join(courses)
#print(course_String) will return History - Math - Physics - CompSci

#String back to list
#new_list = course_String.split(" - ")
#print(new_list) will return ['History', 'Math', 'Physics', 'CompSci']

#Empty lists
#empty_List = []
#empty_lists = list()

print(nums)
print(courses)