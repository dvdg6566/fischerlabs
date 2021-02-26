import urllib.request
from time import time
import json
from mol2 import proc
import os

def getJson(url):
	data = urllib.request.urlopen(url).read()
	return json.loads(data)

def getInfo(compound):	
	print(f"Compound name: {compound}")
	
	# GET SYNONYMS
	synonyms = []
	url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/synonyms/json'	
	SYN_json = getJson(url)['InformationList']['Information'][0]
	CID = SYN_json['CID'] # CID
	SYN = SYN_json['Synonym'] # Synonyms
	print('Synonyms ',SYN[:5])
	print('Compound ID: ',CID)
	# Update lookup DB with syn
	# Update DB with CID

	url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/PNG'
	data = urllib.request.urlretrieve(url,'test.png')
	# Upload to S3

	url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{CID}/property/MolecularFormula,MolecularWeight,IUPACname/json'
	molInfo_json = getJson(url)['PropertyTable']['Properties'][0]
	molFormula = molInfo_json['MolecularFormula']
	molWeight = molInfo_json['MolecularWeight']
	molIUPAC = molInfo_json['IUPACName']
	print("Molecular Formula: ",molFormula)
	print("Molecular Weight: ",molWeight)
	print("IUPAC ",molIUPAC)
	# print(molFormula,molWeight,molIUPAC)

	HSDBindex = -1 # Hazardous substances index
	for i in SYN:
		if(i.find('HSDB')!=-1):
			x = int(i.split(' ')[1])
			HSDBindex = x
	print("HSDB Index: ",HSDBindex)

	if not os.path.isfile(f"{compound}.json"):
		allInfoURL = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{CID}/JSON/'
		alljson = getJson(allInfoURL)
		f = open(f"{compound}.json","w")
		f.write(json.dumps(alljson))
		f.close()
	proc(compound)

getInfo('chlorobenzene')
# getInfo('ethyne')
# getInfo('benzene')
# getInfo('methane')
# getInfo('ethanol')
# getInfo('bromobenzene')
