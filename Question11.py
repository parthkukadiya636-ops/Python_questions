# store the following word meaning in a python dictionary.

Dictionary = {
    "Table": ("a piece of furniture", "list of facts and figures"),
    "cat": "a small animal"
}


print(Dictionary)

"""write a program to enter marks of 3 subjects from the user and store them in the dictionary. start with an empty dictionary and 
add one by one"""
 
marks = {}

x = int(input("Enter phys marks:"))
marks.update({"phy": x})

x = int(input("Enter chem marks:"))
marks.update({"chem": x})

x = int(input("Enter maths marks:"))
marks.update({"maths": x})

print(marks)