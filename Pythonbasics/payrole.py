#name: Joseph Waldron
#payroll program

#step 1 constant variables
REGUALAR_HOURS = 40
OVERTIME_RATE = 1.5
STATE_RATE = 0.03
FED_RATE = 0.02

#step 2 ask user input
name = input('Enter your name: ')
hourlyRate = float(input('Enter your hourly rate: '))
overtimeHours = int(input('Enter overtime hours: '))

#step 3 algorithm
regularPay = hourlyRate * REGUALAR_HOURS
overtimePay = hourlyRate * OVERTIME_RATE * overtimeHours
grossPay = regularPay + overtimePay
stateAmt = grossPay * STATE_RATE
fedAmt = grossPay * FED_RATE
netPay = grossPay - stateAmt - fedAmt

#step 3 display outputs
print('Hello ', name)
print('The regular pay is $', regularPay)
print('The gross pay is $', grossPay)
print('The state tax deduction is $', stateAmt)
print('The federal tax deduction is $', fedAmt)
print('The net pay is $', netPay)