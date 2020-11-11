# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that calculates the average of all the numbers stored in the
# file.

def main():
    infile = open('numbers.txt', 'r')
    line_count = 0
    total = 0
    for line in infile:
        line_count += 1
    infile.close()
    infile = open('numbers.txt', 'r')
    for line in infile:
        amount = float(line)
        total += amount
    average = total / line_count
    print('The average of all of the numbers in the text file is :',average)


main()