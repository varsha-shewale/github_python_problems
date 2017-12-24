import urllib2

f = open('dq_unisex_names.csv','r')
data = f.read()

data_list = [x for x in data.split('\n')]
print data_list[:5]