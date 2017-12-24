
import pandas as pd
import scipy.stats as stats

filepath = "/Users/varsha/Documents/Udacity_DAND_t1t2/Term2/CustomerSupportTime Study.csv"
#with open(filepath) as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row

df = pd.read_csv(filepath)
#print df

nat = df['Nathaly'].values.tolist()
joe = df['Joey'].values.tolist()

t = stats.ttest_ind(nat,joe,equal_var=True)
t = stats.ttest_ind(nat,joe,equal_var=False)

#t = stats.ttest_ind(df['Nathaly'].values.tolist(),df['Joey'].values.tolist(),equal_var=False)
#when equal_var = True -> (array(-2.556971980376697), 0.019808785608032595)
#when equal_var = False -> (array(-2.556971980376697), 0.023124271889437813)

#thus we reject Null hypothesis as p< 0.05. reject H0,
# the null hypothesis that Joey's management style does not have an effect on worker speed

print t
