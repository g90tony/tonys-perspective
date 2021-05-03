from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import Required

class CreateNewArticle(FlaskForm):
    title_label = Markup(" <p class='custom-bold-body mb-0'>Enter article's title</p>")
    category_label = Markup(" <p class='custom-bold-body mb-0'>Select article's category</p>")
    content_label= Markup(" <p class='custom-bold-body mb-0'>Enter article's body</p>")
    
    title = StringField(title_label, validators = [(Required())])
    category = SelectField(category_label, validators = [Required()])
    content = TextAreaField(content_label, validators = [Required(), Email()])
