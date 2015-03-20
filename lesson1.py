print "Watch out, world!"

# ===== variables ===== #
twitter = "@hearmecode"
print twitter

# ====== strings ====== #
print "twitter"
print "My governer's name is Martin O'Malley"

# == new line and tab == #
print "Contact Info:\n Shannon \t shannon@hearmecode.com"
print "Lesson\t\tTopic\n1\t\t\tStrings and Conditionals\n2\t\t\tLists and Loops\n3\t\t\tDictionaries and Files"

# ====== Slicing ====== #
twitter[0]
twitter[1:5]
twitter[:5]
twitter[1:]

phone = "(202) 456-7890"
print phone[1:4]
print phone[6:9]

# == String Formatting == #
name = "Shannon"
age = 29
print "My name is: {0} and my age is: {1}".format(name,age)

phone2 = "202-555-6789"
print "Call {0} for great pizza.".format(phone2[4:])

phone3 = "202-555-9876"
print "-Area Code: {0}\n-Local: {1}\n-Different format: ({0}) {1}".format(phone3[:3],phone3[4:])

# === String Methods === #
email = "shannon@hearmecode.com"
print email.find("@")

twitter = twitter.replace("@", "#")
print twitter

# ===== Functions ===== #
	# len() > length
	# twitter.replace() > replace
	# strip() > removes white space from beginning and end
	# .lower() or .upper() > converts string to lower or uppercase
	# .count() > counts number of times something occurs

# ==== Conditionals ==== #
students = 10
capacity = 50
ta = 5

if students < capacity:
	print "Keep recruiting"
else:
	print "End ticket signups"

if ta == 0:
	print "None? Uh oh!"
elif ta < students / 5:
	print "Keep recruiting TAs"
else:
	print "Aren't the TAs great though?"

####

goal = 100
current_volunteers = 90

if current_volunteers < goal:
	print "You are behind by {0}, work on recruiting!".format(goal - current_volunteers)
elif current_volunteers == goal:
	print "Yay! You have 100 volunteers!"
else:
	print "Its over 100 by {0}!".format(current_volunteers - goal)

