grade = int(input('Enter a grade: '))

while 0 > grade < 100:
    print('Invalid grade')
    grade = int(input('Enter a grade: '))
print('The grade is ', grade)