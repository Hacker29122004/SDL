import pandas as pd
data1={
    'name':['Rohan','Dip'],
    'Id':[23,32],
}
df1=pd.DataFrame(data1)
data2={
    'name':['Jet','Rohit'],
    'Id':[12,26],
}
df2=pd.DataFrame(data2)
combined_df=pd.concat([df1,df2],axis=0)
print(combined_df)
df_merged=df1.merge(df2,left_index=True,right_index=True)
print('\nResult Index Merge:\n',df_merged)