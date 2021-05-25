import utils

_dump_dir= utils.DATA_DIR + "stream_dumps/"

feeds= [
  dict(
    name= "some identifier",
    dir= _dump_dir + "dir", # where to save video fies
    url= "rtsp://user:pass@12.3.4.567:111",
    http_link= "http://12.3.45.678:112",
  ),
  dict(
    # ...
  ),
]

ffmpeg_path= utils.DATA_DIR + "/bin/ffmpeg.exe"