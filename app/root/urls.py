from flask import Blueprint, send_from_directory
from .views import HomeView
import utils


bp= Blueprint('root', __name__)
bp.add_url_rule('/', view_func=HomeView.as_view('home'))


def static(static_type):
	def func(path):
		return send_from_directory(utils.STATIC_DIR + static_type, path)
	return func
bp.add_url_rule('/js/<path:path>', endpoint='js', view_func=static('js'))
bp.add_url_rule('/css/<path:path>', endpoint='css', view_func=static('css'))