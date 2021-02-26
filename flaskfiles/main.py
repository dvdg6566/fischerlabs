from flask import render_template, session, redirect
import awstools

def main():
	userinfo = awstools.getCurrentUserInfo()
	return render_template('main.html',userinfo=userinfo)

