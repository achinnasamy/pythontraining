
import redis


class MarchDataToRedis:


    def saveRedisData(self, twitter_data):

        #print (twitter_data.primary_key + twitter_data.tweeted_text)

        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

        rc = redis.Redis(connection_pool=pool)

        rc.hset(twitter_data.primary_key, "tweeted_text", twitter_data.tweeted_text)
        rc.hset(twitter_data.primary_key, "sentiment_analyzed", twitter_data.sentiment_analyzed)

        # Deletes all the keys
        #rc.flushall()
        #rc.hscan_iter()

        rc.save()
        pool.disconnect()


    def fetchRedisData(self):

        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

        rc = redis.Redis(connection_pool=pool)

        keys = rc.keys("2018-01-04-18-46*")

        for each in keys:
            print rc.hgetall(each)

        pool.disconnect()

