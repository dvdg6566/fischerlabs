from flask import flash,render_template, session, request, redirect
import awstools 

def cost(x):
	ans=0
	for i in x:
		ans += 5*int(i['quantity'])
	return ans

def profile():
	userinfo = awstools.getCurrentUserInfo()
	username = userinfo['username']
	orders=awstools.getOrders(username)
	for order in orders:
		order['cost'] = cost(order['items'])

	currentOrders=[i for i in orders if i['orderedDate'] == -1 or i['orderedDate'] == '-1']
	oldOrders=[i for i in orders if i['orderedDate'] != -1 and i['orderedDate'] != '-1']
	print(len(currentOrders))
	print(len(oldOrders))
	return render_template('profile.html',userinfo=userinfo,currentOrders=currentOrders,oldOrders=oldOrders)

