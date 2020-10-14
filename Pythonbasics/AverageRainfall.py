# Write a program that uses nested loops to collect data and calculate the average rainfall over a
# period of years. The program should first ask for the number of years. The outer loop will
# iterate once for each year. The inner loop will iterate twelve times, once for each month. Each
# iteration of the inner loop will ask the user for the inches of rainfall for that month. After all
# iterations, the program should display the number of months, the total inches of rainfall, and the
# average rainfall per month for the entire period.

years = int(input('Enter number of years: '))
month = 12
total = 0

for yearNum in range(years):
    print('Year number ', yearNum + 1)
    for monthNum in range(month):
        print('Month ', monthNum + 1)
        rainfall = int(input('Rain fall: '))
        total += rainfall

totalMonth = years * 12
average = total / totalMonth
print(totalMonth, " months")
print(total, ' Inches of rainfall')
print('The average is ', average, ' inches.')