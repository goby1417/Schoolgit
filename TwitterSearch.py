'''complexity:
functions to analyse data
see if anyone tweets back'''




from TwitterSearch import *
try:                                                    
    TSearch = TwitterSearchOrder()                      #creating an object of the attributes of the searching guidelines 
    TSearch.set_keywords()                              #==== need the list of keywords (attribute of an object)
    TSearch.set_language('en')                          #set language of tweets to english  
    TSearch.set_include_entities(True)                  #this is the info from the tweets ==== look up what info is involved 

    #token used to connect to my twitter account
    T = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = '')

    for tweet in T.search_tweets_iterable(TSearch):
        print(tweet['user']['screen_name'] + tweet['text']) #this is where the functions will be called to scrape data, maybe to tweet back ? (another api?) ==== research necessary APIs GitHub
