from flask import render_template, session, redirect,flash,request
import awstools
from forms import SignupForm

def signup():
	form = SignupForm()
	userinfo = awstools.getCurrentUserInfo()
	try:
		x = userinfo['username']
		if x != None:
			return redirect('/')
	except:
		pass

	if form.is_submitted():
		result = dict(request.form)

		if result['form_name'] == 'signup':
			username = result['username']
			password = result['password']
			check = awstools.createUser(username,password)
			if check == True:
				flash('Sign Up sucessful! Please Login.','success')
			else:
				flash('Username already taken!','danger')
				result['username'] = ''
				result['password'] = ''
			return redirect('/signup')

	return render_template('signup.html',userinfo=userinfo,form=form)

