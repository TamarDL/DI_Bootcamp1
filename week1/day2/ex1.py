#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s #favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new #variable called our_fav_number
my_fav_numbers = ["12","15","3"]
my_fav_numbers.append("10")
my_fav_numbers.append("100")
my_fav_numbers.remove("100")
print(my_fav_numbers)
my_frienf_fav_numbers = ["13","5"]
our_fav_num = [my_fav_numbers + my_frienf_fav_numbers]
print(our_fav_num)

