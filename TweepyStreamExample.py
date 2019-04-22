import sys
import tweepy
from tweepy import OAuthHandler
from time import sleep
import json

# Important - Don't name file 'tweepy.py'

# Used below to supress problems and continue instead of try/except/continue
from contextlib import suppress

# --- # --------------------------------------------------------------------- # --- #
# --- # --------------------------------------------------------------------- # --- #

# Set True to follow a defined list of twitter users.
# Set False to stream from all accounts based on defined keywords.

FollowerMode = True

# --- # --------------------------------------------------------------------- # --- #
# --- # --------------------------------------------------------------------- # --- #

# --- # ---------------------------------- # --- #
# --- # ---- Follower Mode Dictionary ---- # --- #
# --- # ---------------------------------- # --- #

# Lookup Twitter ID's here https://tweeterid.com/ by entering the accounts @Usernamehandle (without the @)

idsdict = { 'CNN Breaking': 428333,
            'CNN': 759251,
            'NYT': 807095, 
            'Elon Musk': 44196397, 
            'Breaking911': 375721095, 
            'News Breaking': 18112970, 
            'RT': 64643056, 
            'WSJ Breaking News': 23484039,
            'Fox News': 1367531 }

# --- # --------------------------------------------------------------------- # --- #
# --- # --------------------------------------------------------------------- # --- #

# --- # ------------------------------ # --- #
# --- # ---- Search Mode Keywords ---- # --- #
# --- # ------------------------------ # --- #

# --- # ----------------- # --- #
# --- # SEARCH BY KEYWORD # --- #
# --- # ----------------- # --- #

# Example
# search = ['breaking news']

# --- # ---------- # --- #
# --- # SEARCH ALL # --- #
# --- # ---------- # --- #

# [' '] and [''] yields no results. The only way to truly stream all of the tweets (unfiltered)
# requires a connection to the firehose(https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/decahose.html), 
# which is granted only in specific use enterprise cases by Twitter.

search = ['.','a','@','\'','this','to',':(','?','!','$',
          'h','+','_','-','#','b','you', 'c',',','the',
          'i','/','lol','at','this','need','and','RT',
          'if','1', 'd','e','f','g'] # Feel free to expand on this. I believe there's a limit on how much you can add.


# --- # -------------------- # --- #
# --- # SEARCH BY USER INPUT # --- #
# --- # -------------------- # --- #

# search = [input('Enter keyword\n\n')]

# --- # -------------------------------------------------------------- # --- #
# --- # -------------------------------------------------------------- # --- #



# --- # ---------------------- # --- #
# --- # --- AUTHENTICATION --- # --- #
# --- # ---------------------- # --- #

consumer_key = 'YourConsumerKeY'
consumer_secret = 'YourConsumerSecret'
access_token = 'YourAccessToken'
access_token_secret = 'YourAccessTokenSecret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# --- # -------------------------------------------------------------- # --- #
# --- # -------------------------------------------------------------- # --- #

print('Listening for tweets...\n')

if FollowerMode == True:
    # gets all IDs from 'idsdict' and converts them to strings
    ids = [str(i) for i in list(idsdict.values())]

# Main Stream Listener Class
class MyStreamListener(tweepy.StreamListener):
    global ids
    global FollowerMode
    tweets = 0
    
    # on_status is a built in tweepy method to fetch tweets.
    # on_data is another one and shows more detailed information for analytical reasons,
    # but be aware that you will have to parse the json manually like data['text'], data['user']['location'], etc.
    # print out status or data(if using on_data) and run the script to fetch the full JSON to see everything that it can do.
    # You can find a good example of that here https://github.com/varadhbhatnagar/Emoyto
    def on_status(self, status):
        
        # Use this if you plan to use the json functionality below. 
        # If you use this, tab the rest of this class below over by one indent(4 spaces)
        #with open('tweets.json', 'a', encoding='utf-8') as f:
        
        # Supress errors so if that specific tweet has an issue for whatever reason, it will skip it. Similar to try/except.
        # Don't use this if you want to debug/look for issues.
        with suppress(Exception):
            
            userid = str(status.user.id)
            
            # "userid in ids" mentioned below removes all of the mentions and retweets and makes sure it only comes from the original account.
            # Tweepy has no built in way to exclude that to my knowledge based on stackoverflow answers.
            
            if FollowerMode == True and userid in ids:
                
                # You can do this for example - " if status.place.country == 'United States': ",
                # but most people don't have their country listed. status.user.location often shows 'state' or 'city, state' and/or country,
                # but their location is user set so it can really be something made up like 'outer space'. If it's that important,
                # you could always try and use an API to see if it's a valid location.
                
                print('-' * 80)
                
                # Prints the name for this ID that's defined in 'idsdict'
                print(list(idsdict.keys())[list(idsdict.values()).index(int(userid))])
                
                print('User: ' + status.user.screen_name)
                # Attempt to display location and/or country if it exists
                with suppress(Exception):
                    if status.user.location != None and status.user.location != 'None':
                        print('Location: ' + status.user.location)
                with suppress(Exception):
                    print('Country: ' + status.place.country)
                
                # Checks to see if tweet is 'extended'/long. If it is, it will display the full tweet.
                try:
                    text = status.extended_tweet['full_text']
                except AttributeError:
                    text = status.text
                print('Tweet: ' + text)
                sleep(0.015)
                
            elif FollowerMode == False:
                
                print('-' * 80)
                print('User: ' + status.user.screen_name)
                with suppress(Exception):
                    if status.user.location != None and status.user.location != 'None':
                        print('Location: ' + status.user.location)
                with suppress(Exception):
                    print('Country: ' + status.place.country)
                        
                try:
                    text = status.extended_tweet['full_text']
                except AttributeError:
                    text = status.text
                print('Tweet: ' + text)
                
                # Prevents the display from hiccups and keeps the scrolling smooth when scanning all
                sleep(0.016)
                            
            # --- # --------------------------------------------------------------------- # --- #
            # --- # --------------------------------------------------------------------- # --- #
            
            # Optional - Write tweet into json file. You can store just tweets for example
            # Make sure to un-comment the 'with f.open' above and tab the rest of the class below it.
          
            #json_str = json.dumps(status._json)
            #f.write(status.text + '\n')
            
            # --- # --------------------------------------------------------------------- # --- #
            # --- # --------------------------------------------------------------------- # --- #
            
            #  # Optional - Print something out every certain number of tweets to show how many tweets have came through.
            
            #  MyStreamListener.tweets += 1
            # if MyStreamListener.tweets % 1000 == 0:
            #     print(str(MyStreamListener.tweets) + ' Tweets')
            #     for i in range(15):
            #         print(f'|||||||||||||||||||||||||||||||||||----- {MyStreamListener.tweets} ------||||||||||||||||||||||||||||||||||||||| \n')
            #     sleep(1)
                
# Define the listener
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)


if FollowerMode == True:
    stream.filter(follow=ids)
else:
    stream.filter(languages=["en"], track = search )
