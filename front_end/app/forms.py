from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class information_form(FlaskForm):
    s3_bucket = StringField('S3 Bucket Location', validators=[DataRequired()])
    columns = StringField('Columns', validators=[DataRequired()])
    submit = SubmitField('Submit')
