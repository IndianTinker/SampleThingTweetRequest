import requests
print "welcome to the sample thingtweet program"
print "follow the link to get a thingtweet api access key:http://community.thingspeak.com/documentation/apps/thingtweet/"
API_KEY=raw_input("Enter your API key you just fetched")
url="http://api.thingspeak.com/apps/thingtweet/1/statuses/update?api_key="
fill="&status="
url=url+API_KEY+fill
tweet=raw_input("now enter your tweet")
url=url+tweet
print "sending tweet.. .. .. "
response=requests.get(url)
if response.status_code==200:
    print "Tweet sent"
else:
    print "tweet failed due to error="
    print response.status_code
    

    
