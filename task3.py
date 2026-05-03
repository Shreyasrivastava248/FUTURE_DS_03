import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('E:/Github Repositories/Future-interns-intership/FUTURE_DS_03/bank_detail.csv')
# print("import succsusfully")

print(df.head())
print(df.shape)
print(df.describe)
# clean column names
df.columns = df.columns.str.strip().str.lower()

# replace unknown with null
df.replace('unknown', np.nan, inplace=True)

# check null value
print(df.isnull().sum())
# handling null value
df=df.dropna()

# check duplicate
print(df.duplicated(subset=['contact','loan','job']).sum())
# we are not drop the dulpicate data because it make impact on result

# check datatype
print(df.dtypes)

# trim and regx

cat_cols = ['job','marital','education','default','housing','loan','contact','month','poutcome','y']

df[cat_cols] = df[cat_cols].apply(lambda x: x.str.strip().str.upper())

# check invalid  value

cols=['previous','pdays','campaign','duration','day','balance','age']
df = df[(df[cols] >= 0).all(axis=1)]
print((df[cols] < 0).sum())
print("cleaning done")



# save clean dataset

df.to_csv('E:/Github Repositories/Future-interns-intership/FUTURE_DS_03/cleand_dataset.csv',index=False)
print("updated file is saved")