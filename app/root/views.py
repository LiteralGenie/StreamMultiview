from flask import views, request
import utils, config


class HomeView(views.MethodView):
	def __init__(self):
		super().__init__()
		self.template= open(utils.TEMPLATE_DIR + "index.html").read()

	def get(self):
		print(f'home - {request.remote_addr}')
		return utils.render(self.template, feed_config=config.feeds)