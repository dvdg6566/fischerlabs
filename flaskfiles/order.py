from flask import render_template, session, redirect
import awstools

def order(orderID):
	userinfo = awstools.getCurrentUserInfo()
	print(orderID)
	orderinfo = awstools.getOrderInfo(int(orderID))

	if (orderinfo == None):
		return redirect('/')
	print(orderinfo['items'])

	return render_template('order.html',userinfo=userinfo,orderinfo=orderinfo,items=orderinfo['items'])
