try:
    rate = float( input( 'Enter payment rate (wage/hour):' ) )
    hours = float( input( 'Enter hours of work:' ) )

    pay = hours * rate

    print(f'Total pay is: {pay}')

except:
    print('Error, please enter numeric input')