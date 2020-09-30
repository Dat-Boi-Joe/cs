# setting variables
before_tax = input('Enter amount of purchase: ')
state = .05
county = .025

# algorithm
state_total = float(state) * float(before_tax)
county_total = float(county) * float(before_tax)
total_tax = float(county_total) + float(state_total)
total = float(before_tax) + float(total_tax)

# output
print('Amount of purchase: ' + str(before_tax))
print('State tax: ' + '{:.{prec}f}'.format(state_total, prec=2))
print('County tax: ' + '{:.{prec}f}'.format(county_total, prec=2))
print('All tax: ' + '{:.{prec}f}'.format(total_tax, prec=2))
print('Total: ' + '{:.{prec}f}'.format(total, prec=2))
