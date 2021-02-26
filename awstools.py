import boto3
import pubchempy as pcp
from pprint import pprint
from flask import session
from boto3.dynamodb.conditions import Key, Attr
from werkzeug.security import generate_password_hash, check_password_hash

dynamodb = boto3.resource('dynamodb')
compoundSearchTable = dynamodb.Table('compoundSearch')
compoundInfoTable = dynamodb.Table('compoundInformation')
userInfoTable = dynamodb.Table('userInformation')

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

def checkPassword(username, password):
	item = userInfoTable.query(
		KeyConditionExpression = Key('username').eq(username)
	)['Items']
	# Nothing found
	if len(item) == 0:
		return -1
	else:
		hashed = item[0]['password']
		return check_password_hash(hashed,password)

def getCurrentUserInfo():
	try: 
		username = dict(session)['username']
	except KeyError:
		username = None
	return {'username':username,'role':'admin'}

def createUser(username,password):
	item = userInfoTable.query(
		KeyConditionExpression = Key('username').eq(username)
	)['Items']
	if len(item) > 0:
		return False
	else:
		hashed = generate_password_hash(password)
		item = {'username':username,'password':hashed}
		userInfoTable.put_item(Item=item)
		return True

if __name__ == '__main__':
	# pprint(getInventory())
	pprint(getPUBName('ethyne'))
	h = generate_password_hash('hello')
	y = generate_password_hash('hello')
	print(check_password_hash(h,'hello'))
