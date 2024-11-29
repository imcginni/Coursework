import csv

criteria = {"A":[90,100], "B":[80,89], "C":[70,79], "F":[0,69]}
def calc_total(student):
    exams = map(float, student[-3:])
    return max(exams)

def calc_grade(total):
    for k, v in criteria.items():
        if v[0] <=total <= v[1]:
            return k
    return "ERROR"

def print_student(student):
    name = student[0]
    return name
if __name__ == '__main__':
    with open("data/students.csv") as studfile:
        reader = csv.reader(studfile)
        students = list(reader)
    for stud in students:
        name = print_student(stud)
        total = calc_total(stud)
        grade = calc_grade(total)
        print(name, total, grade)

