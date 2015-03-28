# Mapper
import string
from time import strptime

# Mapper 
#########
# Input: a single record
# customer|tier|homeStore|homeStoreLat|homeStoreLon|distance|receipt|datetime|onlineFlag|store|storeLat|storeLon|upc|desc|mupc|subcat|subcat_num|cat|cat_num|dept|dept_num|sales|discount|quantity
# e.g. bdddad32053f7f53031d5dbfdc0692a01837373f|3|66|35.059823|-80.816172|0.8398516561798964|dd4b97177ebb1ea7b6732cc585ac8d0992ae1f87|2014-09-11 21:04:00|0|11|35.053394|-80.848528|00000000008070|24PK RECYCLING FEE|807|REGULAR|55|CARBONATED BEVERAGES|8|BEVERAGE|23|2.0|0.0|1
def mapper(record):
	# Pull out its 'hood and its hour of the day (of 24). Make this the Key: (<'hood>, <hour>)
	record = string.split(record, '|')

	store = int(record[9])
	# 2014-09-11 21:04:00
	recordDateTime = strptime(record[7], "%Y-%m-%d %H:%M:%S")
	hour = recordDateTime[3]
	quantity = int(record[23].strip())

	# Output (<key>, <quantity>)
	# <key> = (hood, hour)
	return [(store, hour), quantity]

# Reducer
##########
# Add up all of the keys

# Use a dict for now. Increment value by one.



def testMapReduce():
	mapOutput = open('map_output.txt', 'w')
	reduced = dict()
	with open('micro_hackathon_data_sample.bsv', 'r') as records:
		records.next()
		count = 0
		for record in records:
			count += 1
			hoodHourCount = mapper(record)
			mapOutput.write(str(hoodHourCount[0]) + '|' + str(hoodHourCount[1]) + '\n')
			if hoodHourCount[0] in reduced:
				reduced[hoodHourCount[0]] += hoodHourCount[1]
			else:
				reduced[hoodHourCount[0]] = 1
			if count == 100:
				break

	# Print Keys and Counts
	reduceOutput = open('reduce_output.txt', 'w')
	for key, value in reduced.items():
		reduceOutput.write(str(key) + '|' + str(value) + '\n')

if __name__ == "__main__":
	testMapReduce()