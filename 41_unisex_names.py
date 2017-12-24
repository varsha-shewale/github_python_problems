'''
Unisex names
For this challenge, you'll be working with the dataset behind this FiveThirtyEight article on common unisex names in
the United States. Unisex names are gender-neutral and both boys and girls share these names.
You'll start by reading in the data and iteratively converting the data into more useful representations.
At the end of this challenge, you'll filter the names to the ones at least 1000 people share.


import urllib2

response = urllib2.urlopen('data/unisex-names/unisex_names_table.csv')
data = response.read()
'''

import csv
import urllib2
import numpy as np

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/unisex-names/unisex_names_table.csv'
response = urllib2.urlopen(url)
data = csv.reader(response)

data_list = []
for row in data:
    data_list.append(row)

#print fulldata_list
data_array = np.array(data_list)

#data_array= data_array[data_array[:, 2].argsort()]
print data_array[1,:]

# a = np.array([[1,4], [3,1]])
# print a
# a.sort(axis=1)
#print a