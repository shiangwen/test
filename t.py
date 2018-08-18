import json

'''
with open('SearchShowAction.json', 'r', encoding='utf-8') as f:
	data = json.load(f)

for show in data:
	# print(show['showInfo'][0]['location'])
	if '台南' in show['showInfo'][0]['location']:
		print(show['title'])

print(type(data))
with open('write_json.json', 'w', encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)

'''
with open('scenic_spot_C_f.json', 'r', encoding='utf-8-sig') as f:
	data = json.load(f)
'''
with open('spot.json', 'w', encoding='utf-8-sig') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)
'''
# print(data)
for spot in data['XML_Head']['Infos']['Info']:
	if spot['Add'] != None:
		if '雲林' in spot['Add']:
			print(spot['Name'], ' : ')
			#print(spot['Description'])
			#print('\n', '='*50, '\n')

