from flask import Blueprint
from .views import AggView
import utils


config= utils.load_yaml(utils.FEED_CONFIG)

bp= Blueprint('feed', __name__)

for i,x in enumerate(config['feeds']):
	base_path= f'feed_{i}'

	agg_view= AggView(x['name'], x['dir'])
	bp.add_url_rule(f'/{base_path}/playlist', view_func=agg_view.playlist_view)
	bp.add_url_rule(f'/{base_path}/video/<string:file_name>', view_func=agg_view.video_view)

# https://github.com/newnewcoder/flask-hls-demo/blob/master/app.py
@bp.after_request
def add_header(response):
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '0'
	return response