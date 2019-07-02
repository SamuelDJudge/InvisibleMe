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
        write_path = form.write_path.data
        columns = form.columns.data
        en_or_de = form.en_or_de.data
        delimiter = form.delimiter.data
        #command = "spark-submit run.py "+str(s3_bucket_location)+" "+str(write_path)+" "+str(columns)+" "+str(en_or_de)+" "+str(delimiter)
        command = "python /Users/samueljudge/Documents/GitHub/InvisibleMe/python/run.py "+str(s3_bucket_location)+" "+str(write_path)+" "+str(columns)+" "+str(en_or_de)+" "+str(delimiter)
        print(command)
        os.system(command)
        return redirect('/success')
    return render_template('form.html', form=form)
