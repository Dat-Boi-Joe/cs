# Roman Numerals
# Write a program that prompts the user to enter a number within the range of 1 through 10. The
# program should display the Roman numeral version of that number. If the number is outside the
# range of 1 through 10, the program should display an error message. The following table shows
# the Roman numerals for the numbers 1 through 10:
# Number Roman Numeral
# 1 I
# 2 II
# 3 III
# 4 IV
# 5 V
# 6 VI
# 7 VII
# 8 VIII
# 9 IX
# 10 X

number = int(input('Enter a number 1-10: '))
if number > 10 or number < 1:
    print('Error number is not 1-10')
elif number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')