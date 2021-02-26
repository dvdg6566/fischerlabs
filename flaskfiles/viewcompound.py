from flask import render_template, redirect
import awstools

def viewcompound(compName):
	compId = awstools.getCompoundCID(compName)
	userinfo = awstools.getCurrentUserInfo()

	return render_template('viewcompound.html',compName=compName,compId=compId,userinfo=userinfo)