#coding=utf8

import config
import library
import processor
import cv2
import data
import sys


def main():

	reload(sys) 
	sys.setdefaultencoding("utf-8")
	init()


def init():

	#init nfs mount
	if 'nfs' == config.data_path_mode:
		print 'mount nfs remote library'
		library.nfs_mount()

	#init albums
	print 'start save all features'
	processor.save_all_features()

	processor.match_all('./imgs/img7.jpg')







if __name__ == '__main__':
	main()