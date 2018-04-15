# encoding: utf-8

import tweepy
import time




# Authentication
consumer_key="8bui1RAkfO52McjXgohQC0f7R"
consumer_secret="T2kPLaxYs0eMxwzGuozzWmci0gpZt9IE100eaLMh7dVO4CiVSk"
access_token="984062390336655360-aNXno208xqFZn3beeCiF6Qc1rFNFkWk"
access_token_secret="R2RXt8O7WY6HWB0swW0y1BgmCta66eahCCBmygSbtwNdV"

# Connection to Twitter STREAM API
auth = tweepy.OAuthHandler("8bui1RAkfO52McjXgohQC0f7R", "T2kPLaxYs0eMxwzGuozzWmci0gpZt9IE100eaLMh7dVO4CiVSk")
auth.set_access_token("984062390336655360-aNXno208xqFZn3beeCiF6Qc1rFNFkWk", "R2RXt8O7WY6HWB0swW0y1BgmCta66eahCCBmygSbtwNdV")
api = tweepy.API(auth)




# Class for the users
class User:
    """ Each candidate is represented by their name
            And their Twitter ID.
    """
# Define attributes
    def __init__(self, twitter_id, first_name, last_name):
        self.id = twitter_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_tweet = 1                 # Request tweets with a higher id than the last one fetched.

# Common errors that can be avoided
ERRORS_TWEEPY = {
    327 :   u'You have already retweeted this tweet.',
    88  :   u'Rate limit exceeded',
    185 :   u'User is over daily status update limit.'
    }

# information specified in lines 23-26 along with details of users associated with "The Americans Tv Series"

USERS = [
        User('546447987',  'TheAmericans',  'FX'),
    User('3588450737',   'Kerirussel',  'Web'),
    User('855103736',   'Matthew',  'Rhys'),
    User('34115555',   'BrandonJ',  'Dirden'),
    User('2318324798',   'Costa',  'Ronin'),
    User('1673982458',   'Keidrich',  'Sellati'),
    User('235213254',   'Holly','Taylor'),
    User('821520293122351104',   'Margo',  'Martindale'),
    User('91126478',   'Noah',  'Emmerich'),
    User('217546128',   'Laurie',  'Holden'),
    User('39974135',   'Scott',  'Ecohen'),
    User('978008242969366528','Gold','jmojt002')

    ]

# Loop - will make sure the code goes on constantly
while True:

# getting tweets for every user (one by one)
        for User in USERS:
            print('Examining {0} {1}...'.format(User.first_name, User.last_name))

# Fetch tweets that have not yet been retweeted (using last_tweet).
            for tweet in api.user_timeline(User.id, since_id=User.last_tweet):

# Fetching a maximum amount of tweets now to avoid fetching as many/the same tweets next time
                User.last_tweet = max(User.last_tweet, tweet.id)

# If we've already retweeted the tweet, let's ignore it
                if tweet.retweeted:
                    print('Tweet {0} is a retweet and will be avoided (It has been retweeted {1} times !).'.format(tweet.id, tweet.retweet_count))
                    continue

# But if we haven't, let's retweet it
                try:
                    api.retweet(tweet.id)
                    print ('Retweet ! : {0}'.format(tweet.text.encode('utf-8')))

# If there's a Tweepy error (listed in lines 30-33, or not), print message in Terminal to let me know
                except tweepy.TweepError as e:
                    print(e.message)

# Update on what is happening in my Terminal
            print('User retweeted. Moving on to the next one.')
        print('All Users have been retweeted for now. Will check again later.')

# To avoid spamming and being blocked by Twitter API
        time.sleep(900)
