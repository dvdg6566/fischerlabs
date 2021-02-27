from flask import render_template, session, redirect,request,flash
import awstools
from forms import Order
import pandas as pd

def order(orderID):
    userinfo = awstools.getCurrentUserInfo()
    print(orderID)
    orderinfo = awstools.getOrderInfo(int(orderID))

    form = Order()

    if (orderinfo == None):
        return redirect('/')
    print(orderinfo['items'])

    cost=0
    for i in orderinfo['items']:
        cost+=5*i['quantity']

    if form.is_submitted():
        result = request.form
        files = request.files

        if result['form_name'] == 'csv_upload':
            if 'order' not in files:
                flash('Order not found', 'warning')
                return redirect(f'/order/{orderID}')
            if files['order'].filename == '':
                flash('Order not found', 'warning')
                return redirect(f'/order/{orderID}')
            file_name = files['order'].filename
            if '.' not in file_name:
                flash('Invalid file format', 'warning')
                return redirect(f'/order/{orderID}')
            ext_file = file_name.rsplit('.', 1)[1].lower()
            if ext_file == 'csv':
                items=orderinfo['items']
                px = pd.read_csv(files['order'])
                x = px.shape[0]
                hdr = list(px.columns.values)
                for i in range(x):
                    name = px[hdr[0]][i]
                    vol = px[hdr[1]][i]
                    done = 0
                    for i in items:
                        if i['compoundName'] == name:
                            i['quantity'] += int(vol)
                            done = 1
                    if not done:
                        items.append({'compoundName':name,'quantity':int(vol),'status':'-'})
                orderinfo['items'] = items
                print(int(orderID))
                awstools.kms(orderID,orderinfo)
                # for i in range(x):

                # awstools.uploadStatement(files['order'], f'{problem_id}.pdf')
                # flash('Uploaded!', 'success')
                # awstools.validateProblem(f'{problem_id}')
                return redirect(f'/order/{orderID}')
            else:
                flash('Invalid file format', 'warning')
                return redirect(f'/order/{orderID}')

    return render_template('order.html',userinfo=userinfo,orderinfo=orderinfo,items=orderinfo['items'],form=form,cost=cost)