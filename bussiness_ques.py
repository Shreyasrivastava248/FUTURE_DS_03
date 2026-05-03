import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('E:/Github Repositories/Future-interns-intership/FUTURE_DS_03/cleand_dataset.csv')

# # Where are users dropping off in the funnel?
# total = len(df)
# print(total)

# engaged = (df['duration'] > 10).sum()
# print(engaged)

# customer = (df['y'] == 'YES').sum()
# print(customer)

# # drop analysis
# drop1 = total - engaged
# print(drop1)

# engaged_rate = (engaged / total) * 100
# print(engaged_rate)

# drop2 = engaged - customer
# print(drop2)

# customer_rate = (customer / engaged) * 100
# print(customer_rate)


# Which channels bring high-quality leads?
high_quality = df.groupby('contact')['y'].apply(lambda x: (x=='YES').mean()*100)
print(high_quality)


# How can conversion rates be improved?

# job_conversion= df.groupby('job')['y'].apply(lambda x:(x=='YES').mean()*100)
# print(job_conversion)

# educ_conv=df.groupby('education')['y'].apply(lambda x:(x=='YES').mean()*100)
# print(educ_conv)

# high_balance_conve=df[df['balance']>df['balance'].median()]
# low_balance_conve=df[df['balance']<=df['balance'].median()]
# high_rate = (high_balance_conve['y'] == 'YES').mean() * 100
# low_rate = (low_balance_conve['y'] == 'YES').mean() * 100

# print(high_rate, low_rate)