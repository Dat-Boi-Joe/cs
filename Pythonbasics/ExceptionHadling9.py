# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# It should handle any IOError exceptions that are raised when the file is opened and data is
# read from it.
# It should handle any ValueError exceptions that are raised when the items that are read
# from the file are converted to a number.
def main():
    line_count = 0
    total = 0
    try:
        infile = open('numbers.txt', 'r')
        for line in infile:
            line_count += 1
        infile.close()
        infile = open('numbers.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        average = total / line_count
        print('The average of all of the numbers in the text file is :',average)
    except IOError:
        print('File not found')
    except ValueError:
        print('A value in the file is not a number')


main()