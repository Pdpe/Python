miles = input("Enter number of miles: ")
yards = input("Enter number of yards: ")
feet = input("Enter number of feet: ")
inches = input("Enter number of inches: ")

totalInches = ((63360 * miles) + (36 * yards) + (12 * feet) + (inches))
totalMeters = totalInches/39.37

kilometers = int(totalMeters/1000)
meters = int(totalMeters-(kilometers*1000))
centimeters = (totalMeters-(kilometers*1000)-(meters))*100

print 'Metric length:'
print kilometers, 'kilometers'
print meters, 'meters'
print round(centimeters,2), 'centimeters'
