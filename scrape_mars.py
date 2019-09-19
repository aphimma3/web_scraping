#!/usr/bin/env python
# coding: utf-8


# In[3]:


from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd


# In[4]:


url = 'https://mars.nasa.gov/news/'
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
response = requests.get(url)


# In[5]:


soup = BeautifulSoup(response.text, 'lxml')


# In[6]:


results = soup.find_all('div', class_='image_and_description_container')


# In[7]:


results[0]
titles = soup.find_all('div', class_='content_title')
pages = soup.find_all('div', class_='rollover_description_inner')
news_title = titles[0].text
news_p = pages[0].text


# In[8]:


print(news_title)


# In[9]:


print(news_p)


# In[10]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(image_url)
html = browser.html


# In[11]:


soup = BeautifulSoup(html, 'html.parser')

sections = soup.find_all('section', class_='primary_media_feature')
a = sections[0].find('article')
print(a['style'])
print('-----------')
jpg = a['style'].split('\'')[1]
featured_image_url = image_url + jpg
print(featured_image_url)


# In[12]:


twitter_url = 'https://twitter.com/MarsWxReport'
browser.visit(twitter_url)
html = browser.html

soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all('li', class_='js-stream-item')
a = items[0]
mars_weather = a.find('p', class_='tweet-text').text
print(mars_weather)


# In[13]:


facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
tables


# In[ ]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]

