from flask import send_file
import cv2, re, time, io, threading


class Feed:
	def __init__(self, url):
		self.url= url
		self.cap= cv2.VideoCapture(url)
		self.last_frame= self.cap.read()[1]

		threading.Thread(target=self.start, args=()).start()

	def start(self):
		while True:
			ret, frame= self.cap.read()
			if ret:
				self.last_frame= frame


feed_dict= {}

def get_feed(url):
	global feed_dict

	if url not in feed_dict:
		feed_dict[url]= Feed(url)
	return feed_dict[url]

# def get_feed_gen(url, encode=True, **kwargs):
# 	cap= get_feed(url)
# 	while cap.isOpened():
# 		ret,frame= cap.read()
# 		if ret:
# 			if encode:
# 				frame= web_encode(frame, **kwargs)
#
# 			yield frame
# 			return

# def web_encode(image, sep="sep", extension="png", mimetype="image/png"):
# 	extension= re.sub(r'^\.*', '', extension)
# 	_,image= cv2.imencode(f'.{extension}', image)
# 	return b'--' + sep.encode() + \
# 		   b'\r\nContent-Type: ' + mimetype.strip().encode() + b'\r\n\r\n' + \
# 		   bytes(image) + b'\r\n'

def web_encode(image, extension="png", mimetype="image/png"):
	extension= re.sub(r'^\.*', '', extension)
	_,image= cv2.imencode(f'.{extension}', image)

	image= io.BytesIO(image)

	return send_file(image, mimetype=mimetype, cache_timeout=-1)

def read_feed(url):
	feed= get_feed(url)
	frame= feed.last_frame
	frame= cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	frame= web_encode(frame)
	return frame