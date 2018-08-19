import json
import requests
'''
url='https://www.metaweather.com/api/location/2306179/2018/7/18/'
response=requests.get(url)
data=json.loads(response.text)
print(type(data))
#print(response.text)
'''
'''
url='https://www.metaweather.com/api/location/2344116/2018/8/16/'
response=requests.get(url)
data=json.loads(response.text)
#print(type(data))
print(data[4]['weather_state_name'])
'''
url='https://docs.python.org/3/index.html'
response=requests.get(url)
print(response.text)
#data=json.loads(response.text)
#print(type(data))
