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

#FOR LOOP
days = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
	print day

for week in range(1, 5): #range(1,5) = [1,2,3,4]
	print 'Week {0}'.format(week)
	# Week 1
	# Week 2
	# Week 3
	# Week 4

#NESTED FOR LOOPS
	#lets combine our 2 for loops
	#watch your indentation!!
for week in range(1,5):
	print "Week {0}".format(week)

	for day in days:
		print day
		#- Week 1 -#
		# Monday
		# Tuesday
		# Thursday
		# Friday
		# Saturday
		# Sunday
		#- Week 2 -#
		# Monday
		# Tuesday
		# Thursday
		# Friday
		# Saturday
		# Sunday
		#- Week 3 -#
		# Monday
		# Tuesday
		# Thursday
		# Friday
		# Saturday
		# Sunday
		#- Week 4 -#
		# Monday
		# Tuesday
		# Thursday
		# Friday
		# Saturday
		# Sunday

#let's add months!
for month in months: #remember, we aready defined months above
	print month

	for week in range (1, 5):
		print 'Week {0}'.format(week)

		for day in days:
			print day
			#== January ==#
			#- Week 1 -#
			# Monday
			# Tuesday
			# Thursday
			# Friday
			# Saturday
			# Sunday
			#- Week 2-#
			# Monday
			# Tuesday
			# Thursday
			# Friday
			# Saturday
			# Sunday
			#- Week 3 -#
			# Monday
			# Tuesday
			# Thursday
			# Friday
			# Saturday
			# Sunday
			#- Week 4 -#
			# Monday
			# Tuesday
			# Thursday
			# Friday
			# Saturday
			# Sunday
			#== February ==#
			#- Week 1 -#
			# Monday
			# Tuesday
			# Thursday
			# Friday
			# Saturday
			# Sunday
			#- Week 2 - #
			# etc, etc through December, you get the idea?

#ENUMERATE
	#enumertate() is a function that you use with a for loop to get the index(position) of that list item
	#commonly used when you need to change each item in a list one at a time
for each_attendee in attendees:
	print "My name is {0}".format(each_attendee)

for my_number, each_attendee in enumerate(attendees): 
	print "My name is {0} and my number is {1}".format(each_attendee, my_number)
	# My name is Shannon and my number is 0
	# My name is Jenn and my number is 1
	# My name is Grace and my number is 2

#ZIP
	#zip() is a function that you use with a for loop to use each item in multiple lists all at once
listOne = ['Aye', 'Bee', 'See']
listTwo = ['One', 'Two', 'Three']

for listOne, listTwo in zip(listOne, listTwo):
	print listOne, listTwo
	# Aye One
	# Bee Two
	# See Three

#WHILE
	#while loops are the cousins of conditionals. like an if statement, while will ask: "Is this true?"
bread = 5

if bread >= 2:
	print "I'm making a sandwhich"

while bread >= 2:
	print "I'm making a sandwhich"
	bread = bread - 2 
	# this will print "I'm making a sandwich" CONTINUOSLY until we reach less than 2 slices of bread. I have 5 slices of bread, so it will print twice.
	# 5 - 2 = 3. 3 - 2 = 1. 1 is < 2 so the while loop stops
else: 
	print "I'm out of bread" #this will print when I reach less than 2 slices


#Understand lists and loops now? go do some playtime exercises for practice!
	# 99 bottles (Beginner): https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_99bottles.py
	# PBJ while (Beginner): https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_pbj_while.py
	# States (Intermediate): https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
	# Movies (Advanced): https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_movies.py