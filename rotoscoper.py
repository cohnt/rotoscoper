import numpy as np
import cv2
import sys
from moviepy.editor import VideoFileClip

def replace_img_with_edges(img):
	return cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2RGB)

def main():
	if len(sys.argv) != 3:
		print("Usage: ./python3 rotoscoper.py [input file] [output file]")
	in_fname = sys.argv[1]
	out_fname = sys.argv[2]
	clip = VideoFileClip(in_fname)
	modified = clip.fl_image(replace_img_with_edges)
	modified.write_videofile(out_fname)

if __name__ == '__main__':
	main()