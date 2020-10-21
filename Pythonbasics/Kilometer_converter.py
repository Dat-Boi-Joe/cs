# The Kilometer Converter Problem
# Write a program that asks the user to enter a distance in kilometers, then converts that distance
# to miles. The conversion formula is as follows:
# Miles=Kilometers×0.6214

def main():
    print('This is a kilometers to miles converter')
    y = input('Enter number of Kilometers: ')
    kilo_converters(int(y))
    print('Finished')

def kilo_converters(x):
    miles = x * 0.6214
    print(x, 'Kilometers is', miles, 'Miles')


main()