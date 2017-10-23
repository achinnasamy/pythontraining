import requests


data = '''
    {
        "name" :"BNP",
        "location": 
                {
                "lat": %d,
                "lon":    5    
                }
    }
'''

range_of_counter = range(800, 1000)


for i in range_of_counter:
    url = 'http://localhost:9200/bgeo/banks/%d?pretty' % i

    for j in range(10,36):
        data = '''
        {
            "name" :"BNP",
            "location": 
                    {
                    "lat": %d,
                    "lon":    -112    
                    }
        }
        ''' % j
    #print url
    response = requests.post(url, data=data)
    print(" The response is  - %s" % response.text)
#print(" The response is  - %s" % response.text)