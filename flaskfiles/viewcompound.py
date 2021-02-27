from flask import render_template, redirect
import awstools

def viewcompound(compound):
	userinfo = awstools.getCurrentUserInfo()
	compoundInfo = awstools.getCompoundDetails(compound)
	compoundInfo['compoundName']=compoundInfo['compoundName'].title()
	HSDB = compoundInfo['HSDBindex']
	compoundInfo['synonyms'] = [i.title() for i in compoundInfo['synonyms']]
	return render_template('viewcompound.html',compoundInfo=compoundInfo,userinfo=userinfo)