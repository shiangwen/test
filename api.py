import requests
'''
url='https://www.dcard.tw/_api/forums/pet/posts?popular=false'
response=requests.get(url)

response_json=response.json()
#很重要

gender={'F':0,'M':0}
for i in response_json:
    #print(i['gender'])
    gender[i['gender']]+=1
print(gender)

'''
#重要練習

url='https://works.ioa.tw/weather/api/all.json'
response=requests.get(url)
data=response.json() #加json就不用編碼
#data=json.loads(response.text)也可以這樣寫！！！！
#print(data[0])
#print(data[1])
#print(data[0]['name'],data[0]['towns']['name'])

for i in range(0,len(data)):
    for j in range(0,len(data[i]['towns'])):
        print(data[i]['name'],data[i]['towns'][j]['name'])

'''
#i就是data[i]
for i in data:
    for j in range(0,len(i['towns'])):
        print(i['name'],i['towns'][j]['name'])
'''


