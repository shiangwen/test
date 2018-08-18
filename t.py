import json

with open('scenic_spot_C_f.json', 'r', encoding='utf-8-sig') as f:
	data = json.load(f)

# print(data)
for spot in data['XML_Head']['Infos']['Info']:
	if spot['Add'] != None:
		if '雲林' in spot['Add']:
			print(spot['Name'], ' : ')
			print(spot['Description'])
			#print('\n', '='*50, '\n')

