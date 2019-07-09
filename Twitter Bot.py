#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common import keys

import time


# In[5]:


class TwitterBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)


# In[10]:


theBotInstance = TwitterBot('twagswag222@gmail.com','schoolbus')
theBotInstance.login()


# In[ ]:




