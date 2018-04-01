
class TwitterData:


    def __init__(self, _primary_key, _tweeted_text,
                 _tweet_created_at,
                 _tweet_processing_date,
                 _screen_name, _location, _sentiment_analyzed):

        self.primary_key = _primary_key
        self.tweeted_text = _tweeted_text
        self.tweet_created_at = _tweet_created_at
        self.tweet_processing_date = _tweet_processing_date
        self.screen_name = _screen_name
        self.location = _location
        self.sentiment_analyzed = _sentiment_analyzed


