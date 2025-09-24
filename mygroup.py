groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))

def filter_students(students, min_avg):
    filtered = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > min_avg:
            filtered.append(student)
    return filtered

min_avg = float(input("Введите минимальный средний балл для фильтрации: "))

print("\nСтуденты со средним баллом выше", min_avg, ":\n")
print_students(filter_students(groupmates, min_avg))