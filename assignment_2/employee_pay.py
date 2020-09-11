rate = float( input( 'Enter payment rate (wage/hour):' ) )
hours = float( input( 'Enter hours of work:' ) )

if hours > 40:
    extra_pay = ( hours - 40 ) * 1.5 * rate
    pay = extra_pay + 40 * rate
else:
    pay = hours * rate

print(f'Total pay is: {pay}')