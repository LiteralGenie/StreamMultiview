import cv2, re


def get_feed_gen(url, encode=True, **kwargs):
	cap= cv2.VideoCapture(url)
	while cap.isOpened():
		frame= cap.read()[1]
		if encode:
			frame= web_encode(frame, **kwargs)
		yield frame

def web_encode(image, sep="sep", extension="jpg", mimetype="image/jpeg"):
	extension= re.sub(r'^\.*', '', extension)
	_,image= cv2.imencode(f'.{extension}', image)
	return b'--' + sep.encode() + \
		   b'\r\nContent-Type: ' + mimetype.strip().encode() + b'\r\n\r\n' + \
		   bytes(image) + b'\r\n'
