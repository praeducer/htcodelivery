# Big Data Analysis

Since this was a big data hackathon, I wanted to dive into the 140+ million rows of purchase data to help prove our go-to-market approach for the app we are proposing. For each row in the data set, these scripts will map the store and purchase hour to the quantity of items purchased at that hour. It uses Python and Spark via PySpark (https://spark.apache.org/docs/0.9.0/python-programming-guide.html).

columns:
```
customer|tier|homeStore|homeStoreLat|homeStoreLon|distance|receipt|datetime|onlineFlag|store|storeLat|storeLon|upc|desc|mupc|subcat|subcat_num|cat|cat_num|dept|dept_num|sales|discount|quantity
```

e.g. row:
```
bdddad32053f7f53031d5dbfdc0692a01837373f|3|66|35.059823|-80.816172|0.8398516561798964|dd4b97177ebb1ea7b6732cc585ac8d0992ae1f87|2014-09-11 21:04:00|0|11|35.053394|-80.848528|00000000008070|24PK RECYCLING FEE|807|REGULAR|55|CARBONATED BEVERAGES|8|BEVERAGE|23|2.0|0.0|1

```

e.g. output
```
(412, 18)|150106
(274, 12)|249119
(182, 20)|144836
(202, 16)|278490
(477, 21)|1578
(340, 22)|36429
(149, 9)|150114
(40, 6)|3071
```


![Alt text](https://raw.githubusercontent.com/praeducer/htcodelivery/master/spark/heatmap_store_hour_quantity_full.png "Visualization of the full data set")
