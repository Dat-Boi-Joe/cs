total = 0
count = 0
grade = int(input('Enter a grade, enter 999 to stop: '))
while grade != 999:
    if 0 <= grade <= 100:
        total = total + grade
        count = count +1
    else:
        print('Invalid grade')

    grade = int(input('Enter a grade, enter 999 to stop: '))

if count > 0:
    average = total / count
    print('Average is ' + str(average))
else:
    print('No valid grades entered')