import pandas as pd
'''this data variable is used to create data like json to manupulate in pandas'''
data = {
    'Name': ['Anas',None, 'Ahmed', 'Aisha'],
    'Age': [25, 30, 35, 28],
    'marital_status': ['Single', 'Married', 'Single', 'Married']
}
# then we have to make dataframe using pd.DataFrame() function and pass the data variable to it
df = pd.DataFrame(data)
print(df)# now we will print the dataframe using print() function

df.to_json('data.json', index = False)#it will create a json file with the name data.json and
# index = False means it will not create index column in the json file
df.to_excel('data.xlsx', index=False)
df.to_csv('data.csv',index = False)

'''now we will explore data wilth head() and tail() function'''
'''print('First 2 rows of the dataframe:')
print(df.head(2))
print('Last 2 rows of dataframe')
print(df.tail(2))'''
print(df.info())