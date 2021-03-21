from flask import Blueprint
from .views import HomeView


bp= Blueprint('root', __name__)
bp.add_url_rule('/', view_func=HomeView.as_view('home'))