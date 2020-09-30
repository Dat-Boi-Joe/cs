length1 = float(input('Enter length of rectangle 1: '))
width1 = float(input('Enter width of rectangle 1: '))
length2 = float(input('Enter length of rectangle 2: '))
width2 = float(input('Enter width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2
print(area1)
print(area2)

if area1 > area2:
    print('Rectangle 1 has a greater area.')
elif area2 > area1:
    print('Rectangle 2 has a greater area.')
elif area1 == area2:
    print('These rectangles have the same area.')