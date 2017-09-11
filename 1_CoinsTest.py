penny = 1
nickel = 5
dime = 10
quarter = 25
q = 0
d = 0
n = 0
p = 0
i = input("Enter an amount of change from 1 cent to 99 cents: ")
i = int(i)

if i>25:
	q = i/quarter
	i %= quarter
if i>=10:
    d = i/dime
    i%=dime
if i>=5:
    n = i/nickel
    i %= nickel
if i>0:
    p = i/penny
    i = 0
print "The coins are %i quarters, %i dimes, %i nickels and %i pennys." %(q , d, n, p)