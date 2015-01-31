"""This scipt will take three input parameters
	1- source directory to scan
	2- destination directory to move files too
	3- hours back you would like to have files move"""

#import python libraries
import subprocess, os, optparse, sys, time, shutil
import datetime
import os.path
import re

#create the global variable of hours in miliseconds
ONEHOUR = 3600

def scanFolder(folder, hoursOld):

	#set the ONEHOUR varas global
	global ONEHOUR

	#create a var that has the hoursold in epoch
	hoursOld = time.time() - (ONEHOUR * hoursOld)

	print hoursOld
	#start the crawl of all folders
	for dirName, subdirList, fileList in os.walk(folder):
		#create a variable with directory stats
		dirStats = os.stat(dirName)

		if dirStats.st_mtime > hoursOld:
			print dirName


def moveFolder(sourcePath, destinPath):
	print sourcePath
	print destinPath

def main():

	#create the parser var with the options
	parser = optparse.OptionParser(usage= '%prog -s <Source Folder Path> -d <Destination Folder Path> -t <age in hours you would like to move')

	#add the source path parser option
	parser.add_option('-s', '--source', dest='source_path',help='This is the path of the source')
	#add the destination path parser option
	parser.add_option('-d', '--destination', dest='destination_path', default=os.getcwd(), help='This is the path of the destination')
	#add the time parser option
	parser.add_option('-t', '--time', dest='hours_back', default=8, help='This is the amount of hours you want to scan back to')
	#export the parser arguments to the options variable
	options, remainder = parser.parse_args()

	#export each argument to its own var
	sourcePath = options.source_path
	destinPath = options.destination_path
	hoursOld = int(options.hours_back)

	if sourcePath == None:
		print parser.usage #Print usage from when we created the parser var with the OptionParser class
		exit(0)

	scanFolder(sourcePath, hoursOld)

if __name__ == "__main__":

	main()

