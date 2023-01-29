class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and course in lector.courses_lec:
            if course in lector.grade_lec:
                lector.grade_lec[course] += [grade]
            else:
                lector.grade_lec[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw(self):
        all_hw = []
        for val in self.grades.values():
            all_hw.extend(val)
        return sum(all_hw) / len(all_hw)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_hw() < other.average_hw()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_hw() <= other.average_hw()
        return False

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_hw() == other.average_hw()
        return False

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_hw()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lec = {}
        self.courses_lec = []

    def average_rate(self):
        all_list = []
        for val in self.grade_lec.values():
            all_list.extend(val)
        return sum(all_list) / len(all_list)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rate() < other.average_rate()
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rate() <= other.average_rate()
        return False

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rate() == other.average_rate()
        return False

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def all_grades_student(list_student, curses_name):
    new_list = []
    for student in list_student:
        new_list.extend(student.grades[curses_name])
    return sum(new_list) / len(new_list)

def all_grades_lec(list_lec, curses_name):
    new_list = []
    for lec in list_lec:
        new_list.extend(lec.grade_lec[curses_name])
    return sum(new_list) / len(new_list)


student1 = Student('Anna', 'Gofman', 'female')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python', 'Git']
student1.grades['Git'] = [10, 9, 10, 10, 10]
student1.grades['Python'] = [10, 10]

student2 = Student('Alena', 'Katkova', 'female')
student2.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Git']
student2.grades['Git'] = [10, 10, 10, 10, 10]
student2.grades['Python'] = [10, 10]

lec1 = Lecturer('Ivan', 'Petrov')
lec1.courses_lec.append("Python")
lec1.courses_lec.append("Git")
student1.rate_lec(lec1, "Git", 10)
student1.rate_lec(lec1, "Python", 9)

lec2 = Lecturer("Anton", "Apanasevich")
lec2.courses_lec.append("Git")
lec2.courses_lec.append("Python")
student1.rate_lec(lec2, "Git", 8)
student1.rate_lec(lec2, "Python", 10)

rew1 = Reviewer("Oleg", "Ivanov")
rew1.rate_hw(student1, "Python", 9)
rew1.rate_hw(student2, "Python", 8)

rew2 = Reviewer("Olga", "Sidorova")
rew2.rate_hw(student1, "Git", 10)
rew2.rate_hw(student2, "Git", 7)

print(student1)
print(student2)

print(lec1)
print(lec2)

print(lec1 != lec2)
print(lec2 > lec1)
print(student2 >= student1)
print(student2 < student1)

print(all_grades_student([student1, student2], 'Git'))
print(all_grades_student([student1, student2], 'Python'))
print(all_grades_lec([lec1, lec2], 'Git'))
print(all_grades_lec([lec1, lec2], 'Python'))

