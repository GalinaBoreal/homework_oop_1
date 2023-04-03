class Student:
    persons = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        Student.persons.append(self)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # оценки от Reviwers

    def _midl(self):
        midl = 0
        for k, v in self.grades.items():
            midl = round((sum(self.grades[k]) / len(self.grades[k])), 1)
        return midl

    def __str__(self):
        return f'Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за домашние задания: {self._midl()}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка. Выберите пару: студент студент или лектор лектор'
        return f'Средний балл за домашние задания {student1.name} {student1.surname} выше,\
чем {student2.name} {student2.surname}: {self._midl() < other._midl()}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    persons = []

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        Lecturer.persons.append(self)
        self.grades = {}  # оценки от Students

    def _midl(self):
        midl = 0
        for k, v in self.grades.items():
            midl = round((sum(self.grades[k]) / len(self.grades[k])), 1)
        return midl

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._midl()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка. Выберите пару: студент студент или лектор лектор'
        return f'Средний балл за лекции {lecturer1.name} {lecturer1.surname} выше,\
чем {lecturer2.name} {lecturer2.surname}: {self._midl() < other._midl()}'


def rate_hw(student, course, grade):
    if isinstance(student, Student) and course in student.courses_in_progress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
    else:
        return 'Ошибка'


class Reviewer(Mentor):
    pass

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def grades_course_students(cours):
    grades = []
    cours_out = False
    for i in Student.persons:
        for k, v in i.grades.items():
            if cours == k:
                cours_out = True
                g = round((sum(i.grades[k]) / len(i.grades[k])), 1)
                grades.append(g)
            else:
                continue
    if cours_out is False:
        return f'Курс {cours} завершен'
    else:
        return f'Средняя оценка за домашние задания по курсу {cours}: {round((sum(grades) / len(grades)), 1)}'


def grades_course_lecturers(cours):
    grades = []
    cours_out = False
    for i in Lecturer.persons:
        for k, v in i.grades.items():
            if cours == k:
                cours_out = True
                g = round((sum(i.grades[k]) / len(i.grades[k])), 1)
                grades.append(g)
            else:
                continue
    if cours_out is False:
        return f'Курс {cours} завершен'
    else:
        return f'Средняя оценка за лекции по курсу {cours}: {round((sum(grades) / len(grades)), 1)}'


student1 = Student('Matthew', 'Bellamy', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['English']

student2 = Student('Christopher', 'Wolstenholme', 'your_gender')
student2.courses_in_progress += ['Python']

student3 = Student('Dominic', 'Howard', 'your_gender')
student3.courses_in_progress += ['Python']

lecturer1 = Lecturer('Freddie', 'Mercury')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('John', 'Deacon')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Brian', 'May')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Roger', 'Taylor')
reviewer2.courses_attached += ['Python']

rate_hw(student1, 'Python', 15)
rate_hw(student1, 'Git', 10)
rate_hw(student2, 'Python', 15)
rate_hw(student2, 'Python', 5)
rate_hw(student3, 'Python', 5.8)
rate_hw(student3, 'Python', 10.8)

student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Git', 10)
student2.rate_hw(lecturer1, 'Python', 10)
student3.rate_hw(lecturer2, 'Python', 10)
student2.rate_hw(lecturer2, 'Python', 8.5)

print(reviewer1, reviewer2, lecturer1, lecturer2, student1, student2, student3, sep='\n\n')
print()
print(student1 > student2)
print()
print(lecturer1 > lecturer2)
print()
print(grades_course_students('Python'))
print(grades_course_students('Git'))
print()
print(grades_course_lecturers('Python'))
print(grades_course_lecturers('Git'))
print(grades_course_lecturers('English'))
print()
