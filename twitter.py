import tweepy
import pandas as pd
import csv

lines = open('secret.txt').read().splitlines()

auth = tweepy.OAuthHandler(lines[6], lines[7])
auth.set_access_token(lines[8], lines[9])

api = tweepy.API(auth)

c = csv.reader(open('nasdaq.csv'))

rows = []
for row in c:
    rows.append(row)

# Enter Hashtag, initial date, and  number of tweets you want to extract in one run
#words = input("Enter Twitter HashTag to search for \n")
#date_since = input("Enter Date since The Tweets are required in yyyy-mm--dd \n")
#numtweet = int(input("Enter number of tweets you want to extract in one run \n"))
#query = input("What symbol you looking for?")


#I'd probably be searching something like a single tweet... fuck, how do I decide which symbol..? 
# maybe each from the list???? My god, this program will take years though...wouldn't it? I'll test it
# if I have to I'll optimize the base libraies.. I hope not though

#we can use number to increase the number of recent tweets, but for now I'm leaving it at the 
#default of 100
def search():
    for X in range(len(rows)):
        x = api.search_tweets(q=rows[X])
        print(x)
















def PRINTTWEETDATA(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")
  
  
# function to perform data extraction
def scrape(words, date_since, numtweet):
      
    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'description', 'location', 'following',
                               'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
      
    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.home_timeline, q=words, lang="en",
                           since=date_since, tweet_mode='extended').items(numtweet)
     
    # .Cursor() returns an iterable object. Each item in 
    # the iterator has various attributes that you can access to 
    # get information about each tweet
    list_tweets = [tweet for tweet in tweets]
      
    # Counter to maintain Tweet Count
    i = 1  
      
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
          
        # Retweets can be distinguished by a retweeted_status attribute,
        # in case it is an invalid reference, except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
          
        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
          
        # Function call to print tweet data on screen
        PRINTTWEETDATA(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
      
    # we will save our database as a CSV file.
    db.to_csv(filename)

def SENTIMENT_SCORE():
    return



search()