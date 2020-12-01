import pandas as pd
df = pd.read_csv("freedata.csv")

df1 = df[df['status'].str.contains('VERIFIED') == True].copy()
# df1 contains only verified elements

df2 = df1[df1['time'].str.contains('days') == True].copy()
# df1 contains days in day not hours

df2['mtime'] = df2['time'].str.split(' ').str.get(0)
df2['mbid'] = df2['bid'].str.split(' ').str.get(0)
# mtime and mbid refers to modified bid and modified time respectively

df2['bid'].str.split(' ').str.get(0)

df2.drop(['time', 'bid'], axis=1, inplace=True)

df2['mtime'] = df2['mtime'].astype(str).astype(int)
df2['mbid'] = df2['mbid'].astype(str).astype(int)

df3.reset_index(inplace=True)
df3.drop(['index'], axis=1, inplace=True)

# df3.loc[10,'link']
for i in range(10):
    print(df3.loc[i+90, 'link'])
