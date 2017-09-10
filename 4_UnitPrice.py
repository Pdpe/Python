price = input('Enter price of item: ' )
print('Enter weight of item in pounds and ounces seperately')
pounds = input('Enter pounds: ')
ounces = input('Enter ounces: ')

lbsToOz = (pounds * 16)
priceperoz = price / ( lbsToOz + ounces )
print 'Price per ounce: ${}'.format(priceperoz)
