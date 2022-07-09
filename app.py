#!/usr/bin/env python
# coding: utf-8

# In[12]:


from flask import Flask, render_template, request


# In[13]:


import joblib


# In[14]:


app = Flask(__name__)


# In[15]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model = joblib.load("regression.jl")
        r = model.predict([[rates]])
        return(render_template("index.html", result = r))
    else:
        return(render_template("index.html", result = "WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




