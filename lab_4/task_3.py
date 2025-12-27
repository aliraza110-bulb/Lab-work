courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

courses["Data Structures"]["Alice"]=90
courses["Data Structures"].pop("Charlie")
print(courses)

courses["Web Development"]={"Henry":92,"Grace":85}

print("Updated Course",courses)

if "Bob" not in courses["Algorithms"]:
    courses["Algorithms"]["Bob"] = 80

courses.pop("Machine Learning")
print("After Removing machine learning ",courses)

if "Data Structures" in courses :
    grades=courses["Data Structures"].values()
    average_grades=sum(grades)/len(grades)

    print("The Average Grade  Is Found To Be ",average_grades)

else:
    print("Course not found")