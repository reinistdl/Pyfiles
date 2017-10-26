import requests
from requests.auth import HTTPDigestAuth
import json

# Replace with the correct URL
url = "http://jsonplaceholder.typicode.com"

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
#payload = {'id': '1'}
#r = requests.get(url + "/comments", params=payload)
#r1 = requests.get(url + "/comments")
#print("URL: " + r1.url + "\n")
#print (r.json())
#print (r1.text)
#print(r1.json()[1]['body'])
print ("Which comment would You like to see?")
a = None
while (isinstance(a, int)!=True):
    my_input = input()
    try:
        a = int(my_input)
    except:
        print ("input number dumbfuck!")
payload = {"id" : ""+ str(a) +""}
request = requests.get(url + "/comments", params=payload)
print(request.url)
print(request.text)
