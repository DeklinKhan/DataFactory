#!/usr/bin/env python
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import numpy as np

# Importing TextBlob
from textblob import TextBlob

labels = ["Bitcoin","Etherium","Litecoin","Dogecoin","XRP","Tether", "Binancecoin","HEXcoin","ShibaInucoin"]
connection_string = "DefaultEndpointsProtocol=https;AccountName=storagehv4rxpowplahi;AccountKey=ALeynFGMWANAVK66k3Wai++7HTsA+dk+SiakSqmeJKf8YKc8OJXz/2qpgdvryjtbSBSXzxdrxssw+AStTjEpWg==;EndpointSuffix=core.windows.net"
container_name = "datafactory"
folder_path = "input/Datasystems"

# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey="pub_2156343c60cc82b4c0f9008b9ced817143164")

for i in labels:
    response = api.news_api(q=i, country="us", language="en")
    articles = []
    
    for x in range(len(response['results'])):
        title = response['results'][x]['title']
        description = response['results'][x]['description']
        link = response['results'][x]['link']
        article = (title, description, link)
        articles.append(article)
        #print(articles)
    
    articlesframe = pd.DataFrame(articles, columns=['title', 'description', 'link']).head()
    articlesframe['polarity'] = articlesframe.description.apply(lambda x: TextBlob(x).polarity if x else None)
    articlesframe['subjectivity'] = articlesframe.description.apply(lambda x: TextBlob(x).subjectivity if x else None)
    articlesframe['sentiment'] = np.where(articlesframe.polarity > 0, 'positive', np.where(articlesframe.polarity < 0, 'negative', 'neutral'))
    file_path = i+'news.csv'
    articlesframe.to_csv(file_path)
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_name = folder_path + '/' + file_path
    
    blob_client = container_client.get_blob_client(blob=blob_name)
    
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    
    print("File uploaded successfully.")


# In[ ]:




