import numpy as np
import cv2
import sys
from moviepy.editor import VideoFileClip

def replace_img_with_edges(img):
	edges = cv2.cvtColor(cv2.Canny(cv2.blur(img, (5,5)), 50, 75), cv2.COLOR_GRAY2RGB)
	return (255 - edges)

def main():
	if len(sys.argv) != 3:
		print("Usage: ./python3 rotoscoper.py [input file] [output file]")
	in_fname = sys.argv[1]
	out_fname = sys.argv[2]
	if in_fname == out_fname:
		print("Please use different input and output filenames.")
		exit(1)
	clip = VideoFileClip(in_fname)
	modified = clip.fl_image(replace_img_with_edges)
	modified.write_videofile(out_fname)

if __name__ == '__main__':
	main()