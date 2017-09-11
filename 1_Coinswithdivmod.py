cents = input('Enter amount of cents 1 to 99 : ')

def make_change(cents):
    
    parts = divmod(cents,25)
    quarters = parts[0]

    cents_remaining = parts[1]
    parts = divmod(cents_remaining, 10)
    dimes = parts[0]

    cents_remaining = parts[1]
    parts = divmod(cents_remaining, 5)
    nickels = parts[0]

    cents_remaining = parts[1]

    print "The coins are %i quarters, %i dimes, %i nickels and %i pennys." %(quarters, dimes, nickels, cents_remaining)

make_change(cents)
