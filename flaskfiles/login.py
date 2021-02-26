from flask import render_template, session, redirect, request, flash
from forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import awstools

def login():
	form = LoginForm()
	userinfo = awstools.getCurrentUserInfo()
	try:
		x = userinfo['username']
		print(x)
		if x != None:
			return redirect('/')
	except:
		pass

	if form.is_submitted():
		result = dict(request.form)

		if result['form_name'] == 'login':
			username = result['username']
			password = result['password']
			check = awstools.checkPassword(username,password)
			if check == True:
				session['username'] = username
				session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
				print(session.get('username'))
				return redirect('/')
			elif check == -1:
				flash('Username not found!','danger')
			else:
				flash('Password Incorrect','danger')
			return redirect('/login')
		elif result['form_name'] == 'signup':
			print("SIGNUP")
			return redirect('/signup')

	return render_template('login.html',form=form,userinfo=userinfo)

