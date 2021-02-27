from flask import render_template, redirect,request,flash
import awstools

def viewcompound(compound):
	userinfo = awstools.getCurrentUserInfo()
	compoundInfo = awstools.getCompoundDetails(compound)
	compoundInfo['compoundName']=compoundInfo['compoundName'].title()
	HSDB = compoundInfo['HSDBindex']
	compoundInfo['synonyms'] = [i.title() for i in compoundInfo['synonyms']]
	current=awstools.getcurrent(userinfo['currentOrder'],compound)
	return render_template('viewcompound.html',compoundInfo=compoundInfo,userinfo=userinfo,current=current)

def addItem():
	userinfo = awstools.getCurrentUserInfo()
	print(request.form)
	comp = request.form['comp']
	currentVal = request.form['currentVal']
	requestId = userinfo['currentOrder']
	awstools.addItem(comp,currentVal,requestId)
	return "Success!"