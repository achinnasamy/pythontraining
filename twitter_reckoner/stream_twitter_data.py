import json

from twitter.oauth import OAuth
from twitter.stream import TwitterStream

#
# Top trending people
# HMSET r_tweet_1 text "Both should work together for the welfare of the state" created_at "Wed Feb 29 19:20:29 +0000 2012"
#
from twitter_reckoner.twitter_data_cleansing import CleanTweets
from twitter_reckoner.twitter_tags import ReadTwitterTags, DataWriter

#
#
#  text
#  created_at
#  tweet_processing_date
#  screen_name
#  phone_number
#  email_id
#  location
#  retweeted_to_person
#  sentiment_analyzed - positive, negative, neutral
from twitter_reckoner.twitter_data_carrier import TwitterData


class FetchRawTwitterData:


    def fetchTwitterData(self):

        ACCESS_TOKEN    = '4493656032-zhJ6hagHhaLy3TjQKb6tSnuO1imDlcOOYlcletE'
        ACCESS_SECRET   = 'cwjjJnqsSQkll4qdPvNMYnQgU3lkOBeo4MJRbuGujAV3u'
        CONSUMER_KEY    = 'O1MENwW8o14QlD4vFxeJSgAld'
        CONSUMER_SECRET = 'lUkCrhP2ct6j7pATtW7DNbAMJqvxoAulSC6zEQ3d2IM1dDDanR'


        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


        twitter_stream = TwitterStream(auth=oauth)

        read_tags = ReadTwitterTags()
        #tags = read_tags.read_twitter_tags("../twitter_reckoner/twitter_tag_filters_stars.py")
        tags = ['rajini']
        #data_writer = DataWriter("/home/dharshekthvel/.tweets")
        data_writer = DataWriter("/root/data/rajini.tweets")

        for each_tag in tags:

            iterator = twitter_stream.statuses.filter(track=each_tag, language="en")

            tweet_count = 999999
            for tweet in iterator:

                tweet_count -= 1

                complete_tweet = json.dumps(tweet)
                processed_tweet = json.loads(complete_tweet)


                import datetime
                now = datetime.datetime.now()

                if 'text' in processed_tweet.keys():
                    twitter_data = TwitterData(now.strftime("%Y-%m-%d-%H-%M-%S"), processed_tweet['text'].lower(),  "NA", "NA", "NA", "NA", "NOT_ANALYZED")




                clean_tweet = CleanTweets()
                rt_removed_tweet = clean_tweet.remove_RT_from_tweet(twitter_data.tweeted_text)
                cleaned_tweet = clean_tweet.remove_unnecessary_info(rt_removed_tweet)

                #redis_data = MarchDataToRedis()
                #redis_data.saveRedisData(twitter_data)

                print ("T - " + cleaned_tweet)
                data_writer.appendDataToFile(cleaned_tweet)

                if tweet_count <= 0:
                        break








