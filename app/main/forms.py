from flask_wtf import FlaskForm
from wtforms import SubmitField

class LoadMoreArticles(FlaskForm):
    loadMore = SubmitField('Load More')
    