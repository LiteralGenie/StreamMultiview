from flask import views, Response
from utils.stream_utils import *


class FeedView(views.MethodView):
	def __init__(self, url):
		super().__init__()
		self.url= url

	def get(self):
		print('getting', self.url)
		return Response(get_feed_gen(self.url), mimetype=f'multipart/x-mixed-replace; boundary=sep')