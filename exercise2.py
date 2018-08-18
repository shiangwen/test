import json

with open('scenic_spot_C_f.json','r',encoding='utf-8') as f :
    data = json.load(f)
    #print(json.dumps(data))
    for i in range (0,len(data)):
        print(data["XML_Head"]["Infos"][i])

    #print(data)
