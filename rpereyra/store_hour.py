# This is a copy of https://github.com/praeducer/htcodelivery/blob/master/spark/mr_store_hour_local.py
# Original author was Paul Prae (@Praeducer)
# Modified for neighborhoods instead of stores by Renato Pereyra (@rpereyra)
#############################################################

# Mapper
import string
from time import strptime

# Reducer
from collections import Counter

# Mapper
#########
# Input: a single record plus neighborhood
# customer|tier|homeStore|homeStoreLat|homeStoreLon|distance|receipt|datetime|onlineFlag|store|storeLat|storeLon|upc|desc|mupc|subcat|subcat_num|cat|cat_num|dept|dept_num|sales|discount|quantity
# e.g. bdddad32053f7f53031d5dbfdc0692a01837373f|3|66|35.059823|-80.816172|0.8398516561798964|dd4b97177ebb1ea7b6732cc585ac8d0992ae1f87|2014-09-11 21:04:00|0|11|35.053394|-80.848528|00000000008070|24PK RECYCLING FEE|807|REGULAR|55|CARBONATED BEVERAGES|8|BEVERAGE|23|2.0|0.0|1
def mapper(record):
    # Pull out its store and its hour of the day (of 24). Make this the Key: (<store>, <hour>)
    record = string.split(record, '|')

    hood = int(record[10])
    # 2014-09-11 21:04:00
    recordDateTime = strptime(record[3], "%Y-%m-%d %H:%M:%S")
    hour = recordDateTime[3]
    quantity = 1

    # Output <key>|<quantity>
    # <key> = (store, hour)
    return ((hood,hour), quantity)

# Reducer
##########
# Too trivial? Just use a lambda in pyspark

def testMapReduce():
    mapOutput = open('map_output.txt', 'w')
    reduced = Counter()
    with open('out_full2.bsv', 'r') as records:
        records.next()
        for record in records:
            storeHourCount = mapper(record)
            mapOutput.write(str(storeHourCount[0]) + '|' + str(storeHourCount[1]) + '\n')
            reduced[storeHourCount[0]] += float(storeHourCount[1])

    # Print Keys and Counts
    reduceOutput = open('reduce_output.txt', 'w')
    for key, value in reduced.items():
        reduceOutput.write(str(key).replace(',', '|').strip('() ') + '|' + str(value) + '\n')

if __name__ == "__main__":
    testMapReduce()
