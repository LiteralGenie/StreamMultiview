from flask import Blueprint
from .views import FeedView
import utils


config= utils.load_yaml(utils.FEED_CONFIG)

bp= Blueprint('feed', __name__)
for i,x in enumerate(config['feeds']):
	bp.add_url_rule(f'/feed_{i}', view_func=FeedView.as_view(x['name'], url=x['url']))
