from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class information_form(FlaskForm):
    s3_bucket = StringField('S3 Bucket Location', validators=[DataRequired()])
    write_path = StringField('Write Path', validators=[DataRequired()])
    columns = StringField('Columns', validators=[DataRequired()])
    en_or_de = StringField('Encryption or Decryption?', validators=[DataRequired()])
    delimiter = StringField('Delimiter (e.g. period, comma, line, tab, or newline)', validators=[DataRequired()])
    submit = SubmitField('Submit')
