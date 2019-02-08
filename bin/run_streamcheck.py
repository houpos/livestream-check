import subprocess
import shlex
import os
import os.path
import json

# 
# Get List of Streams
#
streamlist = []
# Add in the path to your JSON file. 
filepath = os.path.join("../web/data/livestream.json")

# Open and parse through the file. 
# Create an array with the information from the file
with open(filepath, 'r') as json_file:  
    data = json.load(json_file)
    for p in data:
		streamlist.append({  
			'video_title': p['title'],
			'url': p['url'],
			'video_image': p['video_image']
		})

#
# Test if stream is on or off
#
outputStreamList = []
output = '[\n'
for stream in streamlist:
	# for each item in streamlist array, check to see if live stream is playing
	# for more information about ffprobe, see https://ffmpeg.org/ffprobe.html
    ffprobe_command = 'ffprobe -v fatal -show_entries format=start_time -of default=noprint_wrappers=1'
    args = shlex.split(ffprobe_command)
    args.append(stream['url'])
    try:
		#if stream is running, start building a new json file
    	ffprobeOutput = subprocess.check_output(args)
    	output = output + '{\n"title": "' + stream['video_title'] + '",\n'
    	output = output + '"url": "' + stream['url'] + '",\n'
    	output = output + '"video_image": "' + stream['video_image'] + '",\n},'
    except subprocess.CalledProcessError as e:
		#if stream is not running, do nothing.
		pass

#close off the newly formed json file
output = output[:-1] + '\n]'
# path to new file that will hold ONLY running streams.
mypath = os.path.join('../web/data/stream_checker.json')
# write to file. This overwrites the existing file, if there is one.
file = open(mypath, 'w')
file.write(output)
file.close
