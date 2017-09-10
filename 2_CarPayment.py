a = input( 'Enter amount of loan: ')
r = input( 'Enter interest rate (%): ')
n = input( 'Enter the number of years: ')

i = ( r / 1200.0 )
calc = ( i / ( 1.0 - (1.0 + i ) ** ( -12 * n ) ) ) * a

print 'Monthly payment:', round(calc, 2)
