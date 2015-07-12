# ===== LISTS ===== #

#SYNTAX
	# lists are created by placing items inside []
	# items are separated by commas
attendees = ['Shannon', 'Jenn', 'Grace']
	# an empty list looks like this >
people_who_didnt_do_pbj = []

#SLICING
print attendees[0] #Shannon
print attendees[1] #Jenn
print attendees[2] #Grace
print attendees[0:2] #Shannon, Jenn

#LENGTH
print len(attendees) #3
	#or
number_of_attendees = len(attendees)
print number_of_attendees

#ADDING ITEMS
	#list.append() adds an item to the end
attendees_ages = []
attendees_ages.append(28)
print attendees_ages #[28]

attendees_ages.append(27)
print attendees_ages #[28,27]

#CHANGE EXISTING ITEMS
attendees_ages[0] = 29
print attendees_ages #[29,27]

#QUICK EXERCISE
days_of_week = ['Monday', 'Tuesday']
days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
print days_of_week
print len(days_of_week)

#DELETING EXISTING ITEMS
day = days_of_week.pop()
print day #Friday
print days_of_week #['Monday', 'Tuesday', 'Wednesday', 'Thursday']

day = days_of_week.pop(3)
print day #Thursday
print days_of_week #['Monday', 'Tuesday', 'Wednesday']

print days_of_week.pop(1)
print day #Tuesday
print days_of_week #['Monday', 'Wednesday']

#QUICK EXERCISE
months = ['January', 'February']
months.extend(['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print months #['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#list.append() adds ONE to the end
#list.extend() adds many

#ADD/REMOVE FROM THE BEGINNING
	#remove the first month
months.pop(0)
print months #January is gone
	#insert 'January' before index
months.insert(0, 'January')
print months #January is back

#STRINGS TO LISTS
address = '1133 19th ST NW Washington, DC 20036'
address_as_list = address.split(' ')
	#in this example, every time python sees a space, it will use that to know where to split the string into a list (but you can use any character)
print address_as_list #['1133', '19th', 'ST', 'NW', 'Washington,', 'DC', '20036']
print len(address_as_list) #7 > counts as var
print len('address_as_list') #15 counts as string

#MEMBERSHIP
	#the 'in' keyword allows you to check whether a value exists in the list (also works with strings!)
print 'ann' in 'Shannon' #True
python_class = ['Shannon', 'Maddy']
print 'Frankenstein' in python_class #False

#==EXERCISE==#

#create my empty lists for the quadrants
NW = []
NE = []
SW = []
SE = []

#Ask for address
	#raw_input("What is your address? ")
	#What is your address? 8th & F st NW
	#print address
	#8th & F st NW

#Does this address have a quadrant? If so, add that address to the proper list
	#if 'NW' in address.upper():
	#	NW.append(address)
	#elif 'NE' in address.upper():
	#	NE.append(address)
	#elif 'SW' in address.upper():
	#	SW.append(address)
	#elif 'SE' in address.upper():
	#	SE.append(address)
	#else:
	#	print "No quadrant found for this address: {0}".format(address)

#RANGES OF NUMBERS
	#most common: range from 0 to ...
	#use this when you need to do a task a certain number of times
range(5) #[0, 1, 2, 3, 4]
	#range(start, stop)
range(5,10) #[5, 6, 7, 8, 9]
for number in range(10):
	print number