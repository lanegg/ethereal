#-*-coding:utf-8-*-
import config
import os
import sys

def load_all_covers():

	result = []

	for maindir, subdir, file_name_list in os.walk(config.data_local_path):

		for filename in file_name_list:
			if 'cover.jpg' == filename:
				apath = os.path.join(maindir, filename)
				result.append(unicode(apath, "utf-8"))


	return result


def load_medea(path):
	pass
	

def nfs_mount():
	try:

		if not 'nfs' == config.data_path_mode:
			return
			
		nfs_output = os.popen('mount | grep nfs | grep \'' + config.data_remote_path + '\' | grep \'' + config.data_local_path + '\'')
		nfs_mount = nfs_output.read()
		if '' == nfs_mount:
			print 'nfs mount [' + config.data_remote_path + '] to [' + config.data_local_path + ']'
			os.system('mount -t nfs lanegg.synology.me:/volume1/music/library /Users/lanegg/Music/library')

		return True
	except Exception as e:
		print e
		return False
	

