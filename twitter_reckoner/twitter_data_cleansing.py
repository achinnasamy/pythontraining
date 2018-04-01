



class CleanTweets:




    # @rameshlaus @SholinghurNRavi Answer please ??? What is Rajini Orin and Contribution to TN???? https://t.co/pI2MTi2obw

    def remove_https_from_tweet(self, tweet_text):


        return tweet_text


    # rt @teapainusa: remember, trump promised to do for the rest of america what he did for carrier.
    # removed rt from the tweet
    def remove_RT_from_tweet(self, text):
        replaced_text = text.replace('rt', '')
        return replaced_text


    # @brad_laurie: this looks great, is backed by a real world company
    # removes @brad_laurie:
    #
    # i liked a video https://t.co/u1micfeyjf walton!? and the project with 92% market share
    # https://t.co/u1micfeyjf is removed
    def remove_unnecessary_info(self, text):

        at_replaced_text = ' '.join(word for word in text.split(' ') if not word.startswith('@'))
        https_replaced_text = ' '.join(word for word in at_replaced_text.split(' ') if not word.startswith('https'))
        https_replaced_text_again = ' '.join(word for word in at_replaced_text.split(' ') if not word.startswith('https'))
        empty_lines_removed = https_replaced_text_again.replace('\n','').replace('\n','').replace('\n','')
        removed_ampersand = empty_lines_removed.replace('&amp;', '').replace('&amp;', '')
        return removed_ampersand







