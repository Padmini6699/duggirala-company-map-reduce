# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    Rank,Name,Country,Sales,Profit,Assets,MarketValue = datalist

    # print intermediate key-value pairs to standard output
    print(Country,"\t",1)