import pandas as pd
data = {
    'Name': ['Anas', 'Ali', 'Ahmed', 'Aisha'],
    'Age': [25, 30, 35, 28],
    'marital_status': ['Single', 'Married', 'Single', 'Married']
}

df = pd.DataFrame(data)
print(df)

#df.to_json('data.json')
df.to_excel('data.xlsx')