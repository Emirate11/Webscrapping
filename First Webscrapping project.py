#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


# In[11]:


url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
feedback = requests.get(url)
feedback


# In[12]:


meat = BeautifulSoup(feedback.content, "html.parser")
print(meat.prettify())


# In[4]:


movie_name = []
year_of_release = []
imdb_rating = []


# In[5]:


movie_name_list = meat.findAll("div", class_ = "lister-item mode-advanced")
movie_name_list


# In[6]:


for store in movie_name_list:
    movie = store.h3.a.text
    movie_name.append(movie)
    
    year = store.h3.find("span", class_ = "lister-item-year text-muted unbold").text.replace("(", "").replace(")", "")
    year_of_release.append(year)
    
    rating = store.find("div", class_ = "inline-block ratings-imdb-rating").text.replace("\n", "")
    imdb_rating.append(rating)


# In[7]:


imdb_rating


# In[8]:


movie_data = pd.DataFrame({"Name of Movie" : movie_name, "Release Year" : year_of_release, "IMDB Rating" : imdb_rating})


# In[ ]:


movie_data


# In[15]:


print(len(movie_data))

