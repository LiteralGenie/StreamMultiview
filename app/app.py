from flask import Flask
from . import feed, root


app= Flask(__name__)
app.register_blueprint(root.bp)
app.register_blueprint(feed.bp)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")