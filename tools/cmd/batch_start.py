import subprocess, re, time, datetime
from os import path
import utils


## helpers
CONFIG= utils.load_yaml(utils.FEED_CONFIG)
proj_dir= path.realpath("../../") + path.sep

DEBUG=0
stderr= None if DEBUG else subprocess.DEVNULL

get_stream_dir= lambda name: fr"{proj_dir}data\stream_dumps\{name}" + "/"
get_ffmpeg_cmd= lambda name,stream: f"""
ffmpeg \
-fflags nobuffer 
-rtsp_transport tcp 
-i {stream} 
-vsync 0 
-copyts 
-acodec copy
-vcodec copy	 
-movflags frag_keyframe+empty_moov  
-an 
-hls_flags delete_segments+append_list  
-f segment 
-segment_list_flags live  
-segment_time 0.5 
-segment_list_size 10  
-segment_format mpegts  
-segment_list {get_stream_dir(name)}index.m3u8  
-segment_list_type m3u8 
-segment_list_entry_prefix {get_stream_dir(name)} 
{get_stream_dir(name)}%9d.ts 
""".strip().replace("\n", " ")

get_log_file= lambda x: fr"{proj_dir}\tools\cmd\logs\{x}.txt"
get_log_cmd= lambda name: f" 1> {get_log_file(name)} 2>&1"

streams= {
	# "bed": "rtsp://banoi:ThienDinh716@68.0.23.131:1931/videoMain",
	# "dining": "rtsp://banoi:ThienDinh716@68.0.23.131:1934/videoMain",
	# "living": "rtsp://68.0.23.131:10554/tcp/av0_0",
	x['name'] : x['url'] for x in CONFIG['feeds']
}

sequence_regex= re.compile(r"#EXT-X-MEDIA-SEQUENCE:(\d+)")
def check_new_seq(old_index, index_file):
	seq_number= open(index_file).read()
	seq_number= sequence_regex.search(seq_number)
	if not seq_number:
		return False, None
	seq_number= seq_number.groups()[0]

	return seq_number != old_index, seq_number

log_file= open("./log.txt", "w")
def write(x):
	print(x)
	log_file.write(x + "\n")
	log_file.flush()


## start processes
# web_cmd= fr"cd \"{proj_dir}\" & git pull & \"{proj_dir}\venv\Scripts/python.exe main.py\""
# web_cmd+= get_log_cmd("web")
# web_proc= subprocess.Popen(web_cmd, shell=True) # & is shell operator
# write(web_cmd)

stream_procs= { x:{} for x in streams }
for x,y in streams.items():
	cmd= stream_procs[x]['cmd']= get_ffmpeg_cmd(x,y) # + get_log_cmd(x)
	stream_procs[x]['proc']= subprocess.Popen(cmd, stderr=stderr)
	stream_procs[x]['index_file']= get_stream_dir(x) + "index.m3u8"
	stream_procs[x]['last_index']= None
	write(cmd)


## monitor processes
time.sleep(5)
while True:
	if DEBUG: print('checking')
	for name,dct in stream_procs.items():
		# restart if seq number hasnt changed
		try:
			has_new, val= check_new_seq(dct['last_index'], dct['index_file'])
			if not has_new and dct['last_index'] is not None:
				tmp= datetime.datetime.now().strftime("%b %d -- %H:%M")
				write(f'[{tmp}] Stream {name} unresponsive.')
				dct['proc'].kill()
				dct['proc']= subprocess.Popen(dct['cmd'], stderr=stderr)
				dct['last_index']= None
			else:
				dct['last_index']= val
		except PermissionError:
			write(f"Permission error while checking {name}.")
	time.sleep(15)