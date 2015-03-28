# author: Paul Prae
# pyspark --num-executors 4 --executor-cores 4 --executor-memory 4G

import string
from time import strptime
from pyspark import SparkConf, SparkContext

conf = SparkConf()
#sc.setMaster("yarn")
conf.setAppName("MR Store Hour")
conf.set("spark.executor.memory", "4g")
conf.set("spark.executor.cores", "4")
conf.set("spark.executors.instances", "4")
sc = SparkContext(conf = conf)

# Mapper 
#########
# Input: a single record
# customer|tier|homeStore|homeStoreLat|homeStoreLon|distance|receipt|datetime|onlineFlag|store|storeLat|storeLon|upc|desc|mupc|subcat|subcat_num|cat|cat_num|dept|dept_num|sales|discount|quantity
# e.g. bdddad32053f7f53031d5dbfdc0692a01837373f|3|66|35.059823|-80.816172|0.8398516561798964|dd4b97177ebb1ea7b6732cc585ac8d0992ae1f87|2014-09-11 21:04:00|0|11|35.053394|-80.848528|00000000008070|24PK RECYCLING FEE|807|REGULAR|55|CARBONATED BEVERAGES|8|BEVERAGE|23|2.0|0.0|1
def mapper(record):
	# Pull out its store and its hour of the day (of 24). Make this the Key: (<store>, <hour>)
	record = string.split(record, '|')

	store = int(record[9])
	# 2014-09-11 21:04:00
	recordDateTime = strptime(record[7], "%Y-%m-%d %H:%M:%S")
	hour = recordDateTime[3]
	quantity = int(record[23].strip())

	# Output <key>|<quantity>
	# <key> = (store, hour)
	return ((store,hour), quantity)


dataRDD = sc.textFile("/data/full_no_header")
storeHourCounts = dataRDD.map(lambda line: mapper(line)).reduceByKey(lambda a, b: a + b)
storeHourReduction = storeHourCounts.collect()

# Print Keys and Counts
reduceOutput = open('store_hour_reduce_output.txt', 'w')
for value in storeHourReduction:
	reduceOutput.write(str(value[0]) + '|' + str(value[1]) + '\n')
