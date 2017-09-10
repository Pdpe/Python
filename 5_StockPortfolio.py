spy = input('Enter amount invested in SPY: ')
qqq = input('Enter amount invested in QQQ: ')
eem = input('Enter amount invested in EEM: ')
vxx = input('Enter amount invested in VXX: ')

total = (spy + qqq + eem + vxx)
spyPer = (spy / total)
qqqPer = (qqq / total)
eemPer = (eem / total)
vxxPer = (vxx / total)

print 'ETF       Percentage'
print '--------------------'
print 'SPY          {0:.2%}'.format(spyPer)
print 'qqq          {0:.2%}'.format(qqqPer)
print 'eem          {0:.2%}'.format(eemPer)
print 'vxx          {0:.2%}'.format(vxxPer)
print 'TOTAL AMOUNT INVESTED: ${0:,.2f}'.format(total)
