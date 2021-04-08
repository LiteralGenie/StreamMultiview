from flask import views
import utils


class HomeView(views.MethodView):
	def __init__(self):
		super().__init__()
		self.template= open(utils.TEMPLATE_DIR + "home.html").read()

	def get(self):
		print('getting home')
		feed_config= utils.load_yaml(utils.FEED_CONFIG)
		return utils.render(self.template, feed_config=feed_config)