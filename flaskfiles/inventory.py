from flask import flash,render_template, session, request, redirect
from forms import SearchCompoundForm
import awstools 

def inventory():
	form = SearchCompoundForm()

	if form.is_submitted():
		print("Hello")
		result = request.form
		compound = result['compound']

		PUBCompound = awstools.getPUBName(compound)
		if PUBCompound == None:
			flash('Compound not found!', 'danger')
		else:
			PUBCompound.lower()
			return redirect(f'/compound/{PUBCompound}')

	return render_template('inventory.html',compoundInfo=awstools.getInventory(),form=form)

