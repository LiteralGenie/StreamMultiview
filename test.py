import requests, time

def get_stream(url, timeout=30, max_images=10, end_markers=None, memory_length=10):
	if end_markers is None:
		end_markers= [bytes.fromhex(x) for x in ['ff', 'd9', '0d', '0a']]
	memory= [b'0' for x in range(memory_length)]

	def new_file_check(memory):
		n= len(end_markers)
		if memory[-n:] == end_markers:
			return True
		return False

	s= requests.Session()
	start= time.time()

	image_index= 0
	loop_index= 0
	byte_index= 0
	file= None
	with s.get(url, headers=None, stream=True) as resp:
		for c in resp.iter_content():
			if time.time() - start > timeout or \
					image_index >= max_images:
				return

			if file is None or new_file_check(memory):
				if file: file.close()
				file= open(rf"{image_index}.jp2", "wb")
				image_index+=1
				byte_index= 0

			print(end=f"\r{image_index} - {time.time():.1f}")
			if c:
				memory.pop(0)
				memory.append(c)
				file.write(c)

				loop_index+=1
				byte_index+=1

stream_link= "http://68.0.23.131:2010/videostream.cgi?loginuse=banoi&loginpas=ThienDinh716"
get_stream(stream_link)