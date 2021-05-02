This script will take in a video file, and for each frame, it will perform [Canny edge detection](https://en.wikipedia.org/wiki/Canny_edge_detector) and replace the image at that frame with the edge detector output. This achieves a [rotoscoping](https://en.wikipedia.org/wiki/Rotoscoping)-like visual effect.

Usage: `python3 ./rotoscoper.py [input file] [output file]`