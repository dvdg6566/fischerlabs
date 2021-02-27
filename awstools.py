import boto3
from uuid import uuid4
from pprint import pprint
from flask import session
from datetime import datetime
import pubchempy as pcp
from random import randint
from boto3.dynamodb.conditions import Key, Attr
from werkzeug.security import generate_password_hash, check_password_hash

dynamodb = boto3.resource('dynamodb')
compoundSearchTable = dynamodb.Table('compoundSearch')
compoundInfoTable = dynamodb.Table('compoundInformation')
userInfoTable = dynamodb.Table('userInformation')
ordersInfoTable = dynamodb.Table('ordersInformation')

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

def getCompoundDetails(compound):
	items = compoundInfoTable.query(
		KeyConditionExpression = Key('compoundName').eq(compound)
	)['Items']
	return items[0]

def getPUBName(compoundName):
	item = compoundSearchTable.query(
		KeyConditionExpression = Key('searchKey').eq(compoundName)
	)['Items']
	if len(item) != 0:
		return item[0]['compoundName']
	else:
		compound = pcp.get_compounds(compoundName, 'name')
		try:
			return compound[0].synonyms[0].lower()
		except:
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
	print(dict(session))
	try: 
		username = dict(session)['username']
	except KeyError:
		return {'username':None}
	item = userInfoTable.query(
		KeyConditionExpression = Key('username').eq(username)
	)['Items']
	return item[0]

def createUser(username,password):
	item = userInfoTable.query(
		KeyConditionExpression = Key('username').eq(username)
	)['Items']
	if len(item) > 0:
		return False
	else:
		hashed = generate_password_hash(password)
		id = randint(1,100100)
		createOrder(id,username)
		item = {'username':username,'password':hashed,'role':'buyer','currentOrder':id}
		userInfoTable.put_item(Item=item)
		return True

def getOrderInfo(xx):
	# print(xx)
	try:
		item = ordersInfoTable.query(
			KeyConditionExpression = Key('orderID').eq(xx)
		)['Items']
		return item[0]
	except:
		return None

def getCurrentDateTime():
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return dt_string

def createOrder(id,username):
	item = {
		'orderID':id,
		'username':username,
		'items':[], # Item ID and quantity
		'orderedDate':-1, # 8 digit number or -1
		'createdDate':getCurrentDateTime()
	}
	# print(item)
	ordersInfoTable.put_item(Item=item)


def kms(id,item):
	ordersInfoTable.put_item(Item=item)

def getcurrent(order,item):
	# print(order)
	# print(item)
	x = getOrderInfo(order)
	# print(x)
	for i in x['items']:
		if i['compoundName'] == item:
			return i['quantity']
	return 0

def addItem(comp,currentVal,requestId):
	comp = comp.lower()
	while comp[-1] == ' ':
		comp = comp[:-1]
	while comp[0] == ' ':
		comp = comp[1:]
	currentVal=int(currentVal)
	x= getOrderInfo(requestId)
	done = 0
	for i in x['items']:
		if i['compoundName'] == comp:
			i['quantity']=currentVal
			done = 1
	if not done:
		x['items'].append({'compoundName':comp,'quantity':currentVal,'status':'-'})
	ordersInfoTable.put_item(Item=x)

if __name__ == '__main__':
	pprint(getInventory())
	# createUser('test2','test2')
	# print(getOrderInfo(199))
	# updateOrder(1000,[])