from awscreds import *
import boto3

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