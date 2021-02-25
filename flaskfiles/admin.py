from flask import render_template, session, redirect

def admin():
    return render_template('admin.html')