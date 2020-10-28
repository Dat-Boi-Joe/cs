# Suppose you have a certain amount of money in a savings account that earns compound
# monthly interest, and you want to calculate the amount that you will have after a specific
# number of months. The formula is as follows:
# F=P×(1+i)t
# The terms in the formula are:
# F is the future value of the account after the specified time period.
# 356
# P is the present value of the account.
# i is the monthly interest rate.
# t is the number of months.
# Write a program that prompts the user to enter the account’s present value, monthly interest
# rate, and the number of months that the money will be left in the account. The program should
# pass these values to a function that returns the future value of the account, after the specified
# number of months. The program should display the account’s future value.

def main():
    print('This program will compute how much money you will have on an account with compound interest')
    p = float(input('Enter current amount in account: $'))
    i = float(input('Enter the interest rate in decimal form: '))
    t = float(input('Enter the amount of months: '))
    answer = round(future_value(p, i, t), 2)
    print('The total value of your funds in', int(t), 'months will be $' + str(answer))


def future_value(p, i, t):
    formula = p * (1 + i) ** t
    return formula


main()
