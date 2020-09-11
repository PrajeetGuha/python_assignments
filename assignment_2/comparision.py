a = float( input ( 'Enter first number:' ) )
b = float( input( 'Enter second number:' ) )

if a>b:
    print(f'{a} is greater than {b}')
elif a==b:
    print(f'{a} is equal to {b}')
else:
    print(f'{b} is greater than {a}')