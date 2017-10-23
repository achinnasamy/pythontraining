import requests


# Create index
# Remember - Creation of Index is a put()

# url = 'http://localhost:9200/sentiment'
# response = requests.put(url)
#
# print response.text


data = """
            
            {
                   "bank_name":"Credit",
                   "sentiment_score":"9",
                   "sentiment_tweet_count":"1150"
            }

"""

url = 'http://localhost:9200/sentiment/blog/4'
response = requests.post(url, data=data)

print response.text