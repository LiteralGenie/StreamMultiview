from flask import views
import utils


class HomeView(views.MethodView):
	def __init__(self):
		super().__init__()
		self.template= './templates/home.html'

	def get(self):
		return utils.render(self.template)