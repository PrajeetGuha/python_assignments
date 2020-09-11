points = [0.9,0.8,0.7,0.6,0]
grades = ['A','B','C','D','F']

got_point = float(input('Enter your points:'))

for i,point in enumerate(points):

    if got_point >= point and got_point <= 1.0:

        print(f'You got grade {grades[i]}')

    else:
        print('Point out of range.')
        break