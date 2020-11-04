# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that displays all of the numbers in the file.

def main():
    infile = open('numbers.txt', 'r')
    numbers = infile.read()
    infile.close()
    print(numbers)
    print('Finished')


main()
