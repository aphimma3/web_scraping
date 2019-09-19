#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


# In[ ]:





# In[2]:


app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mongo = client.mars_db
mongo.mars_info.drop()


# In[3]:


@app.route("/")
def index():
    info = mongo.db.mars_info.find_one()
    return render_template("index.html", info=info)


# In[4]:


@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.scrape()
    mars_info.update({}, mars_info_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

