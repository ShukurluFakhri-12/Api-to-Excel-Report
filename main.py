import pandas as pd
import requests
import os
url = 'https://jsonplaceholder.typicode.com/posts'
header = {'User-Agent' : 'Chrome browser bot'}
response = requests.get(url, headers=header , timeout=5)
response.raise_for_status()
data = response.json()
df =pd.DataFrame(data)
df.head()
df.info()
df = df.dropna(subset=['userId'])
df['title'] = df['title'].fillna('Untitled content')
df = df.rename(columns={'userId' : 'User_ID' , 'id': 'Post_Id' , 'title' : 'Post_title' , 'body': 'Content_title'})
df.loc[df['Post_title'].str.len() >= 30 , 'Category'] = 'Long_post'
df.loc[df['Post_title'].str.len() <30 , 'Category'] = 'Short_post' 
df = df.sort_values(by='User_ID' , ascending=True)
df.to_excel('API_Analytics_Report.xlsx', index=False)
print("Process Completed! Check your folder for 'API_Analytics_Report.xlsx'")
