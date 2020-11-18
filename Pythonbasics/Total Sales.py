# Design a program that asks the user to enter a store’s sales for each day of the week. The
# amounts should be stored in a list. Use a loop to calculate the total sales for the week and
# display the result.


def main():
    sales = [0, 0, 0, 0, 0, 0, 0]
    i = 0
    total = 0
    while i < 7:
        x = input('Enter sales for day ' + str(i + 1) + ': ')
        sales[i] = float(x)
        i += 1
    z = 0
    while z < 7:
        total += sales[z]
        z += 1

    print('Total sales for the week = ' + str(total))


main()
