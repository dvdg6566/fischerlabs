from awscreds import *
import boto3
import pubchempy as pcp
from pprint import pprint
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
compoundSearchTable = dynamodb.Table('compoundSearch')
compoundInfoTable = dynamodb.Table('compoundInformation')

def writeToDB(DBname, item):
	if DBname == 'compoundSearch':
		compoundSearchTable.put_item(Item=item)
		print("Success! ",item['searchKey'])
	if DBname == 'compoundInformation':
		compoundInfoTable.put_item(Item=item)
		print("Success! ",item['compoundName'])

def getCompoundCID(compoundName):
	return 6324

def getInventory():
	items = compoundInfoTable.scan(
		ProjectionExpression='compoundName,molecularFormula,quantity'
	)['Items']

	items.sort(key=lambda x:x['compoundName'])
	return items

def getPUBName(compoundName):
	
	item = compoundSearchTable.query(
		KeyConditionExpression = Key('searchKey').eq(compoundName)
	)['Items']
	if len(item) != 0:
		return item[0]['compoundName']
	else:
		# compound = pcp.get_compounds(compoundName, 'name')
		# return compound[0].synonyms[0]
		return None

if __name__ == '__main__':
	# pprint(getInventory())
	pprint(getPUBName('ethyne'))