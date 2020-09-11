temperature = float( input( 'Enter temperature:' ) )
unit = input( 'Enter unit (c\\f):').lower()

if unit == 'c':

    fahrenheit = ( ( 9 * temperature ) / 5 ) + 32
    print(f'Temperature in fahrenheit:{fahrenheit}')

elif unit == 'f':

    celsius = ( ( temperature - 32 ) * 5 ) / 9
    print(f'Temperature in celsius:{celsius}')

else:
    print('Wrong unit.')