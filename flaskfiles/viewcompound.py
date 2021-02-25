from flask import render_template, redirect
import databasetools

def viewcompound(compName):
	compId = databasetools.getCompoundCID(compName)

	return render_template('viewcompound.html',compName=compName,compId=compId)