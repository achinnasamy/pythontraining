# import requests
#
#
#
#
# # Create index
#
# url = 'http://localhost:9200/index102'
# response = requests.put(url)
#
# print response.text
#
#
#
#
# #To create a GEO INDEX
#
# url = 'http://localhost:9200/index102/banks/_mapping'
#
# data = """
#
# {
#     "banks": {
#       "properties": {
#         "name": {
#           "type": "string"
#         },
#         "id": {
#           "type": "string"
#         },
#         "location": {
#           "type": "geo_point"
#         }
#       }
#   }}
#
# """
#
# response = requests.put(url, data=data)
# print response.text
#
#
#
# ### Feed the data
#
# data = '''
# {
# "name" :"Goldman Sachs",
#         "location": {
#         "lat": 60.586967,
#         "lon": 15.422058
#
#
#         }
# }
# '''
#
# range_of_counter = range(4000, 5000)
#
#
# for i in range_of_counter:
#     url = 'http://localhost:9200/index102/banks/%d?pretty' % i
#     response = requests.post(url, data=data)
#     print(" The response is  - %s" % response.text)
#
#
#
#
#
#
