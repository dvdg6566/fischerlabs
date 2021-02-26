import os
import json
import random
import urllib.request
import awstools
from decimal import *
from assets.physicalProperties import proc
import urllib

def getJson(url):
	url=urllib.parse.quote(url,safe=':/')
	data = urllib.request.urlopen(url)
	data = data.read()
	return json.loads(data)

def getInfo(compound):	
	compound = compound.lower()
	print(f"Compound name: {compound}")
	
	# GET SYNONYMS

	url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/property/InChI/json'
	CID_json = getJson(url)
	CID = CID_json['PropertyTable']['Properties'][0]['CID']
	print(CID)

	synonyms = []
	url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/synonyms/json'	
	SYN_json = getJson(url)['InformationList']['Information'][0]
	CID = SYN_json['CID'] # CID
	SYN = SYN_json['Synonym'] # Synonyms
	item = {'searchKey':compound,'compoundName':compound}
	awstools.writeToDB('compoundName',item)

	for i in SYN[:100]:
		item = {'searchKey':i,'compoundName':compound}
		awstools.writeToDB('compoundSearch', item)

	print('Synonyms ',SYN[:5])
	print('Compound ID: ',CID)
	# Update lookup DB with syn
	# Update DB with CID

	# url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/PNG'
	# data = urllib.request.urlretrieve(url,'test.png')
	# Upload to S3

	url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{CID}/property/MolecularFormula,MolecularWeight,IUPACname/json'
	molInfo_json = getJson(url)['PropertyTable']['Properties'][0]
	molFormula = molInfo_json['MolecularFormula']
	molWeight = molInfo_json['MolecularWeight']
	molIUPAC = molInfo_json['IUPACName']
	print("Molecular Formula: ",molFormula)
	print("Molecular Weight: ",molWeight)
	print("IUPAC ",molIUPAC)

	HSDBindex = -1 # Hazardous substances index
	for i in SYN:
		if(i.find('HSDB')!=-1):
			x = int(i.split(' ')[1])
			HSDBindex = x
	print("HSDB Index: ",HSDBindex)

	if not os.path.isfile(f"assets/{compound}.json"):
		allInfoURL = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{CID}/JSON/'
		alljson = getJson(allInfoURL)
		f = open(f"assets/{compound}.json","w")
		f.write(json.dumps(alljson))
		f.close()
	physicalProperties = proc(compound)

	molWeight = Decimal(molWeight)
	molWeight = round(molWeight,2)

	item = {
		'compoundName':compound,
		'CID': CID,
		'molecularFormula':molFormula,
		'molecularWeight':molWeight,
		'IUPACName':molIUPAC,
		'HSDBindex':HSDBindex,
		'physicalProperties':physicalProperties,
		'quantity':random.randint(1,1000)
	}

	awstools.writeToDB('compoundInformation', item)

if __name__ == '__main__':
	# getInfo('chlorobenzene')
	# getInfo('ethyne')
	# getInfo('benzene')
	# getInfo('methane')
	# getInfo('ethanol')
	# getInfo('bromobenzene')
	# getInfo('sodium chloride')
	# getInfo('sodium hydroxide')
	# getInfo('potassium hydroxide')
