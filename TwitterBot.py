#!/usr/bin/env python
# coding: utf-8

# ### Import Relevant libraries

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common import keys

import time


# ### The Bot Class (OOP lvl 99999)

# In[ ]:


class TwitterBot:
    # constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
    # the login function    
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        # finds the email field by class name and password field by name
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        # clear the fields in case they're already filled (as they are if you've saved previous login info)
        email.clear()
        password.clear()
        # fills in the email and password
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
    # the function to like tweets    
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        time.sleep(5)
        
        # change the range according to the number of scrolls you want it to do
        for i in range(5):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            # fin the tweet element by class name
            tweets = bot.find_element_by_class_name('tweet')
            # makes a list of tweet links from the scrolled webpage
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            
            for link in links:
                bot.get('https://twitter.com' + link)
                # added a try except case in case the bot is unable to find the heart button
                # prevents crash
                try:
                    # finds the like button, it is labelled as class HeartAnimation
                    bot.find_element_by_class_name('HeartAnimation').click
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(30)
                    
                    
# currently the sleep time is set according to a slow network, decrease it in case of fast internet
# made on 10/07/2019, working rn


# ### Initialize the bot and start working

# In[ ]:


# fill in your email and password at the place of 'email' and 'password' in the line below
# use inverted commas on both sides of email and password as already done
theBotInstance = TwitterBot('email','password')
theBotInstance.login()

# currently the hashtag to search is set to india, change it according to your requirements
theBotInstance.like_tweet('india')

