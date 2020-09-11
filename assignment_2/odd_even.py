a = int( input( 'Enter a number:' ) )

if a % 2 == 0 and a != 0:
    print('Number is even.')
elif a % 2 != 0 and a != 0:
    print('Number is odd.')
else:
    print('Number is zero.')