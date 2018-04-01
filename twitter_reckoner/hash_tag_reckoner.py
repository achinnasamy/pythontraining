




class HashTagReckoner:



    def persistHashTag(self, relevance_to, tweet_text):

        for each_word in tweet_text.split(' '):
            if each_word.startswith("#"):
                print (each_word)

        return