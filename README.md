# HT CoDelivery
This data analysis project was part of a winning submission for the CODE category of HACKATHON clt MMXV. Our team name is HT CoDelivery and we are out to "Deliver Groceries Together." We wanted to find a simple approach that easily integrates with Harris Teeter's way of doing things. Our idea is relatively easy to implement and seemed to align with Harris Teeter's mission. It was also something our team was skilled to pursue in several hours. The code in this repo was used to prove which markets were valuable to pursue first. The code for the web app will be at a different location.

+ HACKATHON clt MMXV Main Site: http://www.hackathonclt.org/
+ Competition Repo: https://github.com/tresata/hackathon2015

### what is a hackathon?
A hackathon is social coding event where programmers, designers and developers collaborate to solve a problem and compete for cash prizes. It's one part party, one part work-your-butt-off overnight battle against the clock

### what is the business problem to be hacked?
predict, model, plan and present the best, most attractive and creative ways to deliver groceries to customers.

### is this a big data hackathon?
YES. While there are countless approaches you could take with the problem statement, we expect each team to utilize the dataset provided in their unique solution. We look forward to seeing what you come up with..

### what does that (actually) mean?
We have pulled, cleaned and scrubbed real-world data and attached it to a relevant business problem (read on for more on what that is). We'll make sure you are well fed and hydrated as you rack those brain cells on how best to solve the problem. The algorithm that optimizes throughput (and can prove it) will win. easy, right?

### is there a tech stack we will be working on?
Yes we will be working on the tech stack that shames all other tech stacks when it comes to Big Data: Hadoop. You will be able to code against the stack using languages like java, scala and python... so you should be able to hack on it!!

### what processing has already been performed on the data?
We have added 2 columns of transaction data from a local grocer. The first is a flag for online orders, and the second is the distance from the customer's reported address to their home store. The dataset is limited to stores in the Charlotte area and customers with a reported residence within 60 miles of their home store. Transaction summary data has been removed including tender, tax, and other non-product records. Purchases of sensitive items have also been removed.

### what format is the data?
The data is in BSV format.

### what do all of the fields represent?
+ customer = unique identifier for a customer household (masked)
+ tier = value segment of customer
+ homeStore = store closest to the customer's address
+ homeStoreLat = latitude of home store
+ homeStoreLon = longitude of home store
+ distance = distance from customer's address to homeStore in miles
+ receipt = unique identifier for a basket checkout (masked)
+ elFlag = Boolean flag indicating if the transaction was completed online ("1") or in-store ("0")
+ datetime = date and time of the transaction
+ store = store number where the customer checked out
+ storeLat = latitude of store where the customer checked out
+ storeLon = longitude of the store where the customer checked out
+ upc = unique product identifier (industry standard) and base product segmentation
+ description = description of upc
+ mupc = ID number for level 2 of product hierarchy
+ subcategory = description for level 3 of product hierarchy
+ subcat_num = ID number for level 3 of product hierarchy
+ category = level 4 of product hierarchy
+ cat_num = ID number for level 4 of product hierarchy
+ department = level 5 of product hierarchy
+ dept_num = ID number for level 5 of product hierarchy
+ quantity = number of units purchased
+ sales = summed dollar value of UPC-level purchase (= unit price * quantity)
+ discounts = summed dollar value of discounts

### what's the prize?
$4000 grand prize for the HACK category, $2,500 runner ups for CODE and freeSTYLE categories
