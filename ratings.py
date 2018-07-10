

def get_rating(file):
	"""Restaurant rating lister."""

	restaurant_list = open(file)

	# Create dictionary
	restaurant_rates = {}

	# Strip the line by ":"
	for line in restaurant_list:
		line = line.rstrip()
		line = line.split(":")

		# Loop over the file to populate dictionary	
		for item in line:
			restaurant_rates[line[0]] = line[1]
	
	# adding new restaurant submissions
	add_restaurants(restaurant_rates)

	# separate line 24-29 into a separate function (sorting restaurants and printing phrase)
	# create a list of they keys and sort
	alphabetical_restaurants = sorted(restaurant_rates.items())

	# loop over the dictionary to get key's values
	for restaurant, rating in alphabetical_restaurants:
		print("{} is rated at {}".format(restaurant, rating))

	# put your code here


def add_restaurants(restaurant_dict):

	restaurant_input = input("What restaurant would you like to rate? ").title()
	rating_input = int(input("What would you rate the restaurant from 1 - 5? "))

	while rating_input < 1 or rating_input > 5:
		rating_input = int(input("Please enter a number from 1 to 5: "))

	# restaurant_rating = tuple(restaurant_input, rating_input)
	restaurant_dict[restaurant_input] = rating_input

	# restaurant_rates[new_restaurant] = new_rating


get_rating("scores.txt")



# def get_rating(file):
# 	"""Restaurant rating lister."""

# 	restaurant_list = open(file)

# 	# Create dictionary
# 	restaurant_rates = {}

# 	# Strip the line by ":"
# 	for line in restaurant_list:
# 		line = line.rstrip()
# 		line = line.split(":")

# 		# Loop over the file to populate dictionary	
# 		for item in line:
# 			restaurant_rates[line[0]] = line[1]
	
# 	new_restaurant = input("What restaurant would you like to rate? ").title()
# 	new_rating = input("What would you rate the restaurant? ")

# 	restaurant_rates[new_restaurant] = new_rating
	

# 	# create a list of they keys and sort
# 	alphabetical_restaurants = restaurant_rates.keys()
# 	alphabetical_restaurants = sorted(alphabetical_restaurants)

# 	# loop over the dictionary to get key's values
# 	for restaurant in alphabetical_restaurants:
# 		rating = restaurant_rates[restaurant]
# 		print("{} is rated at {}".format(restaurant, rating))

# 	# put your code here

# get_rating("scores.txt")
