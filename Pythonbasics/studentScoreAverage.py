num_students = int(input("How many students: "))
while num_students < 0:
    print('Invalid number of students')
    num_students = int(input("How many students: "))
num_exams = int(input('Number of exams for each student: '))
while num_exams < 0:
    print('Invalid number of exams')
    num_exams = int(input('Number of exams for each student: '))

for students in range(num_students):
    total = 0
    print('Student number', students + 1)
    print('_________________')
    for test_num in range(num_exams):
        print('Test number', test_num +1)
        score = float(input(': '))
        while score < 0 or score > 100:
            print('Please enter a valid grade')
            score = float(input('Enter a rest score: '))
        total += score

    average = total / num_exams
    print('The average score for student number', students + 1, 'is ', average)