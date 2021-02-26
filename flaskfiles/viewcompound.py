from flask import render_template, redirect
import awstools

def viewcompound(compName):
	compId = awstools.getCompoundCID(compName)

	return render_template('viewcompound.html',compName=compName,compId=compId)