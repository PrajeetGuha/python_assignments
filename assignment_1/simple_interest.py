principal = int( input( 'Principal amount:' ) )
rate = float( input( 'Rate of interest:' ) )
years = int( input( 'Years:' ) )

simple_interest = ( principal * rate * years ) / 100

total = principal + simple_interest

print( 'Total:', round( total, 3 ) )