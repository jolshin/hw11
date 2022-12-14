class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Method for setting grades for lectureres by students"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        """Method for calculating the average grade of students"""
        average_grade = 0
        index = 0

        for key, value in self.grades.items():
            for i in range(len(value)):
                average_grade += value[i]
                index += 1

        return str(average_grade/index) 

    def __str__(self):
        """Reformed string method"""
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + \
                self.average_grade() + '\nКурсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + \
                '\nЗавершенные курсы: ' + ', '.join(self.finished_courses)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def average_grade(self):
        """Method for calculating the average grade of lecturers"""
        average_grade = 0
        index = 0

        for key, value in self.grades.items():
            for i in range(len(value)):
                average_grade += value[i]
                index += 1
        
        return average_grade/index

    def __str__(self):
        """Reformed string method"""
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(self.average_grade())

    def __lt__(self, other):
        """Reformed < method"""
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        """Reformed <= method"""
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        """Reformed > method"""
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        """Reformed >= method"""
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        """Reformed == method"""
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        """Reformed != method"""
        return self.average_grade() != other.average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Method for setting grades for students homeworks"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        """Reformed string method"""
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname 

def hws_average_grade(students, course):
    """Function for calculating the homeworks average grade for a certain course"""
   
    students_list = students.split(', ')
    grade = 0
    counter = 0
    mapped_list = []

    for i in range(len(students_list)):
        mapped_list.append(name_mapping[students_list[i]])

    for student in mapped_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                for value in student.grades[course]:
                    counter += 1
                    grade += value
    
    print(f'Средняя оценка студентов по курсу {course} составляет {str(grade/counter)}')   

def lects_average_grade(lects, course):
    """Fucntion for calculating the lecturers average grade for a certain course"""
       
    lects_list = lects.split(', ')
    grade = 0
    counter = 0
    mapped_list = []

    for i in range(len(lects_list)):
        mapped_list.append(name_mapping[lects_list[i]])

    for lecturer in mapped_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                for value in lecturer.grades[course]:
                    counter += 1
                    grade += value
    
    print(f'Средняя оценка лекторов по курсу {course} составляет {str(grade/counter)}') 

def lects_compare():
    """Function for test output of reformed comparison methods"""
    print('\nСранвение лекторов:')
    print('>: ' + str(first_lecturer < second_lecturer))
    print('>=: ' + str(first_lecturer <= second_lecturer))
    print('<: ' + str(first_lecturer > second_lecturer))
    print('<=: ' + str(first_lecturer >= second_lecturer))
    print('==: ' + str(first_lecturer == second_lecturer))
    print('!=: ' + str(first_lecturer != second_lecturer))

def helper(comm):
    """Function for displaying necessary information for working with program in terminal"""
    if comm != 'help':
        print('\nКоманда \"'+comm+'\" не поддерживается')
    
    print('\n--------------------------------------------------\nСписок доступных команд:' +\
            '\nstuds - функция подсчета оценки за домашнее задание по всем студентам в рамках курса' + \
            '\nlects - функция подсчета средней оценки за лекции всех лекторов в рамках курса' +\
            '\ncompare - функция вывода результатов сравнения лекторов'+\
            '\nmethods - вызов метода __str__ вывода классов Student, Lecturer, Reviewer'+\
            '\ncode - исполнение кода exec(compile(code_goes_here, \'compile() code\', \'exec\'))'+\
            '\nhelp - вывод справки' +\
            '\nquit - выход' +\
            f'\nСписок доступных имен студентов и лекторов: {", ".join(name_mapping.keys())}' +\
            '\n--------------------------------------------------\n')

def mapper():
    """Function to replace input strings with object names"""
    global name_mapping

    name_mapping = {
        'Archer Sterling' : first_student,
        'Lana Kane' : second_student,
        'Melory Archer' : first_lecturer,
        'Cyril Figgis' : second_lecturer
    }

def main():
    """Main function"""

    mapper()

    helper('help')

    while True:
        comm = input('Введите команду:')

        if comm.lower() == 'studs':
            hws_average_grade(input('Введите список студентов (имя фамилия, ...) через запятую: '), input('Введите наименование курса: '))
        elif comm.lower() == 'lects':
            lects_average_grade(input('Введите список лекторов (имя фамилия,...) через запятую: '), input('Введите наименование курса: '))
        elif comm.lower() == 'compare':
            lects_compare()
        elif comm.lower() == 'methods':
            print(f'Список студентов: \n{first_student}\n{second_student}\n\nСписок лекторов:\n{first_lecturer}\n{second_lecturer}'+\
                f'\n\nСписок проверяющих:\n{first_reviewer}\n{second_reviewer}\n')
        elif comm.lower() == 'code':
            code = input('Введите код для исполнения, например \"print(first_student)\": ')
            exec(compile(code, 'compile() code', 'exec'))
        elif comm.lower() == 'help':
            helper(comm)
        elif comm.lower() == 'quit':
            print('Выход')
            break
        else:
            helper(comm)

"""Creation of the objects and calling their methods"""
first_student = Student('Archer', 'Sterling')
second_student = Student('Lana', 'Kane')

first_reviewer = Reviewer('Adam', 'Reed')
second_reviewer = Reviewer('Matt', 'Thompson')

first_lecturer = Lecturer('Melory', 'Archer')
second_lecturer = Lecturer('Cyril','Figgis')

first_reviewer.courses_attached += ['Python', 'PEP 8', 'OOP', 'GIT']
second_reviewer.courses_attached += ['GIT', 'OOP', 'Python', 'PEP 8']

first_student.courses_in_progress += ['Python', 'GIT', 'OOP']
first_student.finished_courses += ['PEP 8']

second_student.courses_in_progress += ['OOP', 'PEP 8', 'Python']
second_student.finished_courses += ['GIT']

first_reviewer.rate_hw(first_student, 'Python', 4)
first_reviewer.rate_hw(first_student, 'PEP 8', 3)
first_reviewer.rate_hw(first_student, 'OOP', 3)
second_reviewer.rate_hw(first_student, 'GIT', 5)
second_reviewer.rate_hw(first_student, 'OOP', 4)

first_reviewer.rate_hw(second_student, 'Python', 5)
first_reviewer.rate_hw(second_student, 'PEP 8', 5)
second_reviewer.rate_hw(second_student, 'GIT', 4)
second_reviewer.rate_hw(second_student, 'OOP', 3)

first_lecturer.courses_attached += ['OOP', 'PEP 8']
second_lecturer.courses_attached += ['Python', 'GIT']

first_student.rate_lecturer(first_lecturer, 'OOP', 3)
first_student.rate_lecturer(first_lecturer, 'PEP 8', 4)
first_student.rate_lecturer(second_lecturer, 'Python', 5)
first_student.rate_lecturer(second_lecturer, 'GIT', 4)

second_student.rate_lecturer(first_lecturer, 'OOP', 4)
second_student.rate_lecturer(first_lecturer, 'PEP 8', 5)
second_student.rate_lecturer(second_lecturer, 'Python', 3)
second_student.rate_lecturer(second_lecturer, 'GIT', 5)


"""Calling the main function"""
main()