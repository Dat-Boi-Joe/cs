# A bug collector collects bugs every day for five days. Write a program that keeps a running total
# of the number of bugs collected during the five days. The loop should ask for the number of
# bugs collected for each day, and when the loop is finished, the program should display the total
# number of bugs collected.

counter = 1
total_bugs = 0
while counter < 6:
    bugs = input('Bugs found on day ' + str(counter) + ' : ')
    counter += 1
    total_bugs += int(bugs)
print(str(total_bugs) + ' total bugs.')