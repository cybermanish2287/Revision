#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy 
from tweepy import OAuthHandler # to authenticate Twitter API
from tweepy import Stream 
# These next two libraries are actually native to python which means we don't need to pip install them
import socket 
import json 


# In[2]:


# Twitter developer Credentials to connect to twitter account
# These are no longer active so you need to set up a Twitter Developer Account to get your own
access_token = "1211654595165880321-OJjzdNfCJhS6hZ0CBqC4YpizEup4cQ"
access_secret = "meyV3ACTolG4qVGVhLoA5Ad9HSorSVyjXUEqcPXnKAEtX"
consumer_key = "A05qH7ex13v6g0he93MekudDs" # API key
consumer_secret = "JSJuccBkacnESO38U5s3QbKqNtjB5jezuEUIVOHWV4rR0F97dS" # API secret key
# An access token used in authentication that allows you to pull specific data.
bearer_token = "AAAAAAAAAAAAAAAAAAAAAM1acgEAAAAAnlSzuuP766ndgmKiRMZ7nEMzVgs%3Dq17EwG9fBPQttTgcO80hbCaO0iz7SEolbU7MOmqwKyT3c1mvA5"


# In[3]:


class TweetsListener(tweepy.Stream):
    # initialized the constructor
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            # read the Twitter data which comes as a JSON format
            msg = json.loads(data)

            # the 'text' in the JSON file contains the actual tweet.
            # We will encode this with utf-8 which will clean out any emojis and stuff that may cause errors for us
            # We can come back and change this later on if we need to
            print(msg['text'].encode('utf-8'))

            # the actual tweet data is sent to the client socket
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True

        except BaseException as e:
            # Error handling
            print("Ahh! Look what is wrong : %s" % str(e))
            return True
    # If there actually is an error, we will print the status
    def on_error(self, status):
        print(status)
        return True


# In[4]:


# if __name__ == '__main__':
# create a socket object
s = socket.socket()


# In[5]:


# Get local machine name : host and port
host = "127.0.0.1"
# You'll want to make sure this port is being used elsewhere, otherwise you'll get an error
port = 3350


# In[6]:


# # Bind to the port
s.bind((host, port))
print("Listening on port: %s" % str(port))


# In[7]:


# Wait and Establish the connection with client.
s.listen(5)
# This sends us back a tuple with the data and the addresss where it came from
c, addr = s.accept()


# In[8]:


# # Let's print it so we can confirm that when we are at the command line
 print("Received request from: " + str(addr))


# In[9]:


# authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# twitter_stream will get the actual live tweet data
# This is a stream object
twitter_stream = Stream(auth, TweetsListener(c))
# filter the tweet feeds related to "corona"
twitter_stream.filter(track=['corona'])
# in case you want to pass multiple criteria
# twitter_stream.filter(track=['DataScience','python','Iot'])


# In[ ]:




