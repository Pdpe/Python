fv = input( 'Enter face value of bond: ' )
intr = input( 'Enter coupon interest rate as a decimal:' )
mp = input( 'Enter the current market price: ')
years = input( 'Enter the years until maturity: ')

fv = float(fv)
mp = float(mp)
years = float(years)

a = ( fv - mp ) / years
b = ( fv + mp ) / 2.0

ytm = ( ( intr * 1000.0) + a ) / b

print ('Approximate YTM: {0:.2%}'.format(ytm))
