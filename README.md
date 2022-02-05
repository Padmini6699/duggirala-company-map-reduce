# duggirala-piping-map-reduce
I am practising mapping and reducing.

# Type of data
For this assignment I have used the dataset that gives the list of top companies that has the following columns: country name, company name, sales, profits, asserts and market value. Since 2003 this data set gives the list for about 12 months in the year 2021.

# Analysis
I have six columns in the data set which describe the sales and profits of various companies in different countries. By using the mapping reducing and sorting techniques I initially had 2001 rows which have been reduced to 61 rows and I have filtered in excel using top 10 count. And inserted the 2D Bar chart.

# Following commands to run the script 

For Mapping

```cat fortune2021.csv | Python 01mapper.py > output.txt```

For reducing

```cat fortune2021.csv | Python 01mapper.py | sort | Python 01reducer.py > duggirala-output.txt```

# Chart
<img width="372" alt="alphabetical" src="https://user-images.githubusercontent.com/77808223/152584393-345742a7-414e-4e99-865a-17f4f1372c82.PNG">



