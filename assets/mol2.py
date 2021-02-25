import json

headers = ['Boiling Point',
	'Melting Point',
	'Solubility',
	'Density',
	'Vapor Density',
	'Vapor Pressure',
	"Heat of Vaporization",
	"Heat of Combustion",
	'Viscosity'
]

def scan(physical, title):
	for i in physical:
		th = i['TOCHeading']
		if th == title:
			res = i['Information'][0]['Value']['StringWithMarkup'][0]['String']
			return res

def proc(compound):
	with open(f'{compound}.json','r') as file:
		data = json.load(file)

	data = data['Record']['Section']

	physical = data[3]['Section'][1]
	# print(physical)

	# print(physical['TOCHeading'])

	physical = physical['Section']
	
	res = []
	for i in headers:res.append(scan(physical,i))
	physicalProperties = {}
	for i in range(len(headers)):
		physicalProperties[headers[i]] = res[i]
		print(headers[i]+':', res[i])

	print()
	return physicalProperties

# proc('ethyne')
# proc('benzene')
# proc('methane')
# proc('ethanol')
# proc('bromobenzene')


# print(dat)
# print(json.dumps(physical)[:100])