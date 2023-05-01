from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    original_url = URLField('Вставьте ссылку', validators=[DataRequired(message="Поле не должно быть пустым"),
                                                           URL(message="Здесь должна быть валидная ссылка!")])
    submit = SubmitField('Получить короткую ссылку')
