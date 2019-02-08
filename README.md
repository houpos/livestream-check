# livestream-check
Reads a JSON file of m3u8 URLs, uses ffprobe to check if streams are running, then outputs running streams to a new JSON file.

## Use
I created and used this script and JSON file for these smart TV apps: [Apple TV](https://itunes.apple.com/us/app/goarch/id1270174561?ls=1&mt=8), [Amazon Fire TV](https://www.amazon.com/gp/product/B07DPV3FKY), and [Roku](https://my.roku.com/add/GOARCH).

The app shows Greek Orthodox churches that live stream their services. The purpose of the script was to create a "Now Playing" section so viewers could quickly find a running stream.

streamchecker.py was placed on a server and a cron job was created to run the script every 15 mins, which updates stream_checker.json. 

When a user opens the Apple TV

## Getting Started
1. To run in your local environment, install ffprobe. You can with [npm](https://www.npmjs.com/package/ffprobe).
2. Also, install [Python](https://www.python.org).
3. Update livestream.json with your stream information, including a URL to your video. You can add more JSON objects or key/value pairs. 
4. If you changed or added keys in livestream.json, open streamchecker.py and update or add the keys where needed. Look around lines 20 - 22.
5. Update both os.path.join() lines with the correct path. Depending on your OS, you may have change how the path is written. See https://docs.python.org/3/library/os.path.html

## Running
* On your local environment, you can run the script with just ***py streamchecker.py***
* On a server, add streamchecker.py as a cron job to run as often as needed.
