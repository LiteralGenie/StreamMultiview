import utils
from flask import views, Response, make_response, send_from_directory
from utils.stream_utils import *


class PlaylistView(views.MethodView):
	def __init__(self, video_dir):
		super().__init__()
		self.video_dir= video_dir

	def get(self):
		playlist_file= self.video_dir + "index.m3u8"
		playlist= open(playlist_file).read()
		playlist= re.sub(r".:.*?([^/\\]+ts)", rf"video/\1", playlist)

		return Response(playlist, content_type="application/vnd.apple.mpegurl")

class VideoView(views.MethodView):
	def __init__(self, video_dir):
		super().__init__()
		self.video_dir= video_dir

	def get(self, file_name):
		resp= make_response(send_from_directory(directory=self.video_dir, filename=file_name))
		return resp

class AggView:
	def __init__(self, name, video_dir):
		self.name= name
		self.video_dir= video_dir

	@property
	def playlist_view(self):
		return PlaylistView.as_view(f"{self.name}_playlist",
									video_dir=self.video_dir)

	@property
	def video_view(self):
		return VideoView.as_view(f"{self.name}_video",
								 video_dir=self.video_dir)