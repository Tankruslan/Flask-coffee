from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, Email


class EmailForm(FlaskForm):
    email = StringField('', validators=[Length(1, 64), Email()],
                        render_kw={"placeholder": "Ваш e-mail"})
