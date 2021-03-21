from flask import Flask
from blueprints import feed, root


app= Flask(__name__)
app.register_blueprint(root.bp)
app.register_blueprint(feed.bp)
app.run(debug=True)