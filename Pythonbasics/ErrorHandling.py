def Value_error():
    complete = False
    while not complete:
        try:
            hours = int(input('How many hours: '))
            pay_rate = float(input('Hourly rate: '))
            gross_pay = pay_rate * hours
            print("GrossPay: $", gross_pay)
            complete = True
        except ValueError:
            print("Error: Hours and pay rate must be valid numbers")


# input output
def io_Error():
    filename = input('Enter a file name: ')

    try:
        infile = open(filename, 'r')
        content = infile.read()
        print(content)
        infile.close()
    except IOError:
        print("No file Found")


def allerrors():
    total = 0.0
    try:
        infile = open('numbers.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(total)
    except ValueError:
        print('A value is incorrect in the file')
    except IOError:
        print("No file Found")
    except:
        print('An error occurs')
    finally:
        print('The end')



