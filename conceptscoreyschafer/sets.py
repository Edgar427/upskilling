cs_courses = {"History" , "Math", "Physics", "CompSci"}
art_courses = {"History" , "Math", "Art", "Design"}



#sets are used to remove duplicate, to test if a value is part of a set
#print("Math" in cs_courses)  returns a boolean if something is in the set

#what courses these sets have in common
#print(cs_courses.intersection(art_courses))

#what courses are in cs_courses but not in art_courses
#print(cs_courses.difference(art_courses))


#if you want to combine both sets
#print(cs_courses.union(art_courses))

#Empty sets
#empty_set = {} This is WRONG , its a dict
#empty_set = set()