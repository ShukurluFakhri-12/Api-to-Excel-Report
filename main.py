import pandas as pd
import requests
import logging
logging.basicConfig(filename = "api_analiz.log" 
                    , level = logging.INFO ,
                    format='%(asctime)s | %(levelname)s | %(message)s')
def api_to_excel():
  try:
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
    df = df.rename(columns={'userId' : 'User_ID' ,
                            'id': 'Post_Id' 
                            , 'title' : 'Post_title' ,
                            'body': 'Content_title'})
    df.loc[df['Post_title'].str.len() >= 30 , 'Category'] = 'Long_post'
    df.loc[df['Post_title'].str.len() <30 , 'Category'] = 'Short_post' 
    df = df.sort_values(by='User_ID' , ascending=True)
    df.to_excel('API_Analytics_Report.xlsx', index=False)
    logging.info("Process Completed! Check your folder for 'API_Analytics_Report.xlsx'")
  except requests.exceptions.RequestException as error:
    logging.info(f'Error in API or Internet : {error}')
  except Exception as e:
    logging.info(f'The Error Found: {e}')
   
api_to_excel()
