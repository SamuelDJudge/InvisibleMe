from flask import render_template, request, redirect
from app import app
from app.forms import information_form
import os


@app.route('/success')
def success():
    return render_template('index.html', title='Success')

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def login():
    form = information_form()
    if form.validate_on_submit():
        s3_bucket_location = form.s3_bucket.data
        columns = form.columns.data.split(',')
        os.system('ls')
        return redirect('/success')
    return render_template('form.html', form=form)
