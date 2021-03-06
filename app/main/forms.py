from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Required

class LoadMoreArticles(FlaskForm):
    loadMore = SubmitField('Load More')
    
    
class AddComment(FlaskForm):
    comment_input = TextAreaField('', validators=[Required()])
    submit = SubmitField('Post')
    