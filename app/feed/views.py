from flask import views, Response
from utils.stream_utils import read_feed


class FeedView(views.MethodView):
	def __init__(self, url):
		super().__init__()
		self.url= url

	def get(self):
		return read_feed(self.url)