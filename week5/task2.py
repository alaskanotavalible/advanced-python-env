import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)

with open("students_with_average.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)