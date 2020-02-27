'''
Joseph Waldron
Assignment 1
'''

#1 Write a program that asks the user for his/her first name and last name. Then print out the user’s name in the following format: last name, first name

'''first_name = input('First name: ')
last_name = input('Last name: ')
print('Hello, '+last_name+', '+first_name)'''

#2  Write a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

'''name = input('Name: ')
age = input('Age: ')
when100 = 2020+(100-int(age))
print(name+', you will be 100 years old in '+str(when100))'''

#3 Write a program that asks the user to enter 2 numbers to divide. Print out a message telling them what the remainder is.

'''divide = input('Number to divide: ')
divideby = input('Number to divide by: ')
answer = int(divide)%int(divideby)
print(str(divide)+' divided by '+divideby+' will give a remainder of '+str(answer))'''

#4 Write a program that asks the user to enter a word and how many times they want the word to be repeated. Print that word to the screen as many times as they requested, with a space in between the words.

'''string = input('Word: ')
number = input('How many times: ')

while int(number) > 0:
    print(string)
    number = int(number)-1'''

#5 Write a program that asks the user to enter the length and width of a rectangle. Print out a message telling them what the area and perimeter are.

'''length = input('Length: ')
width = input('Width: ')
area = int(length)*int(width)
perimeter = int(length)*2+int(width)*2
print('Area: '+str(area))
print('Perimeter: '+str(perimeter))'''

#6 Write a program that asks the user to enter the diameter of a circle. Print out the circumference and area of the circle.

'''from math import pi
diameter = input('Diameter: ')
circumf = 2*pi*(.5*int(diameter))
area = pi*(.5*int(diameter))**2
print('The area is '+str(area) +', and the circumference is '+str(circumf))'''

#7 Write a program that asks the user to enter the year in which they were born. Print out a message telling them how old they are.

'''year = input('What year were you born?: ')
print('You are '+str(2020-int(year)-1)+' years old')'''

#8 Write a program that asks the user to enter a number. Print out that number squared.

'''number = input('Number: ')
print(str(number)+' squared is '+str(int(number)**2))'''

#9  Write a program that asks the user to enter a number of hours. Print out how many seconds that is.

'''hours = input('Hours: ')
sec = int(hours)*60**2
print(str(hours)+' hours is '+ str(sec)+' seconds.')'''