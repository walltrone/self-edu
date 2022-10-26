class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_value(self):
        if not self.grades:
            return 0
        grades_list = []
        for grades_enu in self.grades.values():
            grades_list.extend(grades_enu)
        grades_avg = sum(grades_list) / len(grades_list)
        return round(grades_avg, 1)

    def __str__(self):
        some_student = f'Имя: {self.name} \nФамилия: {self.surname}' \
                       f'\nСредняя оценка за ДЗ: {self.average_value()}' \
                       f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
                       f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return some_student

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_value() == other.average_value()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_value() < other.average_value()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_value() < other.average_value()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        some_lecturer = f'Имя: {self.name} \nФамилия: {self.surname}' \
                        f'\nСредняя оценка за лекции: {self.average_value()}'
        return some_lecturer

    def average_value(self):
        if not self.grades:
            return 0
        grades_list = []
        for grades_enu in self.grades.values():
            grades_list.extend(grades_enu)
        grades_avg = sum(grades_list) / len(grades_list)
        return round(grades_avg, 1)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_value() == other.average_value()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_value() < other.average_value()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_value() < other.average_value()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_reviewer


def student_grades_average(students, course):
    if not isinstance(students, list):
        return "Студенты не обнаружены"
    grades_list = []
    for student in students:
        grades_list.extend(student.grades.get(course, []))
    if not grades_list:
        return "По такому курсу ни у кого нет оценок"
    grades_avg = sum(grades_list) / len(grades_list)
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {round(grades_avg, 1)}'


def lecturer_grades_average(lecturers, course):
    if not isinstance(lecturers, list):
        return "Студенты не обнаружены"
    grades_list = []
    for lecturer in lecturers:
        grades_list.extend(lecturer.grades.get(course, []))
    if not grades_list:
        return "По такому курсу ни у кого нет оценок"
    grades_avg = sum(grades_list) / len(grades_list)
    return f'Средняя оценка за лекции по всем лекторам в рамках курса {course}: {round(grades_avg, 1)}'


first_student = Student('Marie', 'Curie', 'female')
first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('William', 'Wallace', 'male')
second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['Введение в программирование']

first_lecturer = Lecturer('Vladimir', 'Lenin')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Iosif', 'Dzhugashvili')
second_lecturer.courses_attached += ['Git']

first_reviewer = Reviewer('John', 'Doe')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Jane', 'Doe')
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 10)

second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 9)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'Git', 9)

first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(first_lecturer, 'Python', 9)
first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(second_lecturer, 'Git', 10)
first_student.rate_lec(second_lecturer, 'Git', 10)
first_student.rate_lec(second_lecturer, 'Git', 10)
first_student.rate_lec(second_lecturer, 'Git', 10)

second_student.rate_lec(first_lecturer, 'Python', 10)
second_student.rate_lec(first_lecturer, 'Python', 10)
second_student.rate_lec(first_lecturer, 'Python', 8)
second_student.rate_lec(first_lecturer, 'Python', 10)
second_student.rate_lec(second_lecturer, 'Git', 10)
second_student.rate_lec(second_lecturer, 'Git', 9)
second_student.rate_lec(second_lecturer, 'Git', 10)
second_student.rate_lec(second_lecturer, 'Git', 10)

print(first_student)
print()
print(second_student)
print()
print(first_lecturer)
print()
print(second_lecturer)
print()
print(first_reviewer)
print()
print(second_reviewer)
print()
print(student_grades_average([first_student, second_student], 'Python'))
print(student_grades_average([first_student, second_student], 'Java'))
print(student_grades_average([first_student, second_student], 'Git'))
print(lecturer_grades_average([first_lecturer, second_lecturer], 'Python'))
print(lecturer_grades_average([first_lecturer, second_lecturer], 'Git'))
print()
print(first_student < second_student)
print(second_lecturer > first_lecturer)
print(first_student == first_lecturer)
