
#A quicker binary search which infers the data's slope to jump ahead and perform the beginning binary search, presumably closer to the data being looked for

import random
import math

array = random.sample(range(1, 500), 480)

array.sort()

print(array)

def quick_binary(array, sample, search_value):

	# grab sample data points from list
	sample_size = array[:sample]
	print(sample_size)

	# add the data points
	sum_sample = sum(sample_size)

	# calculate 'slope' by dividing the number of data points in sample size by its sum
	slope = sum_sample / len(array[:sample])
	#print(slope)

	# find starting point by dividing the search value by the slope
	begin_binary = math.floor(search_value // slope)
	print(begin_binary)

	# take sample size into consideration
	if search_value < sample_size[-1]:
		if len(array) == 0:
			return - 1
		low = 0
		high = len(sample_size) - 1
		print("sample", high)

		while low < high:
			x = low + (high - low) // 2
			val = array[x]
			if search_value == val:
				return x
			elif search_value > val:
 				if low == x:
 					break
 				low = x
			elif search_value < val:
 				high = x

		return - 1
	else:
  		if len(array) == 0:
  			return - 1
    
  		low = len(sample_size)
  		high = len(array[begin_binary:]) - 1
  		print("rest", high)

  		while low < high:
  			x = low + (high - low) // 2
  			val = array[x]
  			if search_value == val:
  				return x
  			elif search_value > val:
  				if low == x:
  					break
  				low = x
  			elif search_value < val:
  				high = x

	return - 1

quick_binary(array, 50, 18)

