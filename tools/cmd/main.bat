set proj_dir=C:\Programming\StreamMultiview
start "web server" cmd /k "cd %proj_dir% & git pull & %proj_dir%\venv\Scripts/python.exe main.py"
start "bed" cmd /k "ffmpeg  -fflags nobuffer    -rtsp_transport tcp    -i rtsp://banoi:ThienDinh716@68.0.23.131:1931/videoMain   -vsync 0    -copyts    -vcodec copy    -movflags frag_keyframe+empty_moov    -an    -hls_flags delete_segments+append_list    -f segment    -segment_list_flags live    -segment_time 0.5    -segment_list_size 10    -segment_format mpegts    -segment_list %proj_dir%\data\stream_dumps/bed/index.m3u8    -segment_list_type m3u8    -segment_list_entry_prefix %proj_dir%\data\stream_dumps/bed/   %proj_dir%\data\stream_dumps/bed/%%9d.ts"
start "dining" cmd /k "ffmpeg  -fflags nobuffer    -rtsp_transport tcp    -i rtsp://banoi:ThienDinh716@68.0.23.131:1934/videoMain   -vsync 0    -copyts    -vcodec copy    -movflags frag_keyframe+empty_moov    -an    -hls_flags delete_segments+append_list    -f segment    -segment_list_flags live    -segment_time 0.5    -segment_list_size 10    -segment_format mpegts    -segment_list %proj_dir%\data\stream_dumps/dining/index.m3u8    -segment_list_type m3u8    -segment_list_entry_prefix %proj_dir%\data\stream_dumps/dining/   %proj_dir%\data\stream_dumps/dining/%%9d.ts  "
start "living" cmd /k "ffmpeg  -fflags nobuffer    -rtsp_transport tcp    -i rtsp://68.0.23.131:10554/tcp/av0_0   -vsync 0    -copyts    -vcodec copy    -movflags frag_keyframe+empty_moov    -an    -hls_flags delete_segments+append_list    -f segment    -segment_list_flags live    -segment_time 0.5    -segment_list_size 10    -segment_format mpegts    -segment_list %proj_dir%\data\stream_dumps/living/index.m3u8    -segment_list_type m3u8    -segment_list_entry_prefix %proj_dir%\data\stream_dumps/living/   %proj_dir%\data\stream_dumps/living/%%9d.ts"

cmd /k

"""
ffmpeg
-fflags nobuffer
-rtsp_transport tcp
-i rtsp://banoi:ThienDinh716@68.0.23.131:1934/videoMain
-vsync 0
-copyts
-vcodec copy
-movflags frag_keyframe+empty_moov
-an
-hls_flags delete_segments+append_list
-f segment
-segment_list_flags live
-segment_time 0.5
-segment_list_size 10
-segment_format mpegts
-segment_list C:\Users\Anne\PycharmProjects\StreamMultiview\data\stream_dumps/dining/index.m3u8
-segment_list_type m3u8
-segment_list_entry_prefix C:\Users\Anne\PycharmProjects\StreamMultiview\data\stream_dumps/dining/
C:\Users\Anne\PycharmProjects\StreamMultiview\data\stream_dumps/dining/%9d.ts
"""