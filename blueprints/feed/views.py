from flask import views, Response
from utils.stream_utils import get_feed_gen


class FeedView(views.MethodView):
	def __init__(self, url):
		super().__init__()
		self.url= url
		self.sep= 'sep'

	def get(self):
		return Response(get_feed_gen(self.url, sep=self.sep),
						mimetype=f'multipart/x-mixed-replace; boundary={self.sep}')