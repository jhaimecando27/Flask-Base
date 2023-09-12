from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegiserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('EMail', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(),
                             Length(min=8),
                             EqualTo('confirm')])
    comfirm = PasswordField('Confirmation Password', validators=[
                            DataRequired(), Length(min=8)])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
