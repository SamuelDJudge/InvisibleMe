#Imports
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
        file = open("/home/ubuntu/InvisibleMe/src/system_info.csv","w+")
        for info in [s3_bucket_location, write_path, en_or_de, delimiter,columns]:
            if info == columns:
                file.writelines(info)
            else:
                file.writelines(info+",")
        command = "spark-submit /home/ubuntu/InvisibleMe/src/run.py"
        os.system(command)
        return redirect('/success')
    return render_template('form.html', form=form)
