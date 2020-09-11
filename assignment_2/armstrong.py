number = input('Enter the number:')

sum = 0

for d in number:

    sum += int(d)**3

if sum == int(number):
    print('Number is armstrong.')
else:
    print('Number is not armstrong.')