# LIST-mutable
stud=["Evelyne","Nathan","Cathy","Jude","Patrick"]
print(stud)
stud[0]="Brian"
stud.append("Ndungu")
stud.sort()
print(stud)
print(f"My name is {stud[0]}")

# TUPLE-immutable
fruits=("Bananas","Watermelon","Pineapple","Oranges")
print(fruits)
fruits.count("Bananas")
print(fruits.count("Bananas"))

# SET
cars={"toyota","mercedes","nissan","rangerover"}
print(cars)

# DICTIONARY
employees={"name":"Evelyne","salary":20000, "age":24}
print(employees)
print("name is %s"%employees["name"])
print("salary is %d"%employees["salary"])
print("age is %d"%employees["age"])