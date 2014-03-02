#!/usr/bin/env python

#
# organize.py --help for documenation
#

import os, sys, re, time, argparse, logging

def init_logging():
	logger = logging.getLogger('organize')
	logger.setLevel(logging.INFO)
	# create file handler which logs even info messages
	lf = logdir + '/' + log_file
	fh = logging.FileHandler(lf)
	fh.setLevel(logging.INFO)
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)
	# add the handlers to logger
	logger.addHandler(ch)
	logger.addHandler(fh)
	return logger

def read_config():
	mappings.clear()
	try:
		cf = confdir + '/' + conf_file
		file = open(cf)
	except:
		logger.error(conf_file + " cannot be found, exiting")
		exit(1)
	while 1:
		line = file.readline()
		if not line:
			break
		match_obj = re.match(r'(.+):(.+)', line, re.M | re.I)
		if match_obj == None:
			continue
		matches = match_obj.groups()
		mappings[matches[0]]=matches[1]

def parse(line):
	match_obj = re.match(r'\[\[(.+)\]\](.+)', line, re.M | re.I)
	if match_obj == None:
		directories = [line[0].lower()]
		filename = line
	else:
		matches = match_obj.groups()
		directories = [matches[0][0]]
		directory = mappings.get(matches[0])
		if directory != None:
			directories.append(directory.lower())
		filename = matches[1]
	return (directories, filename)

def organize():
	for filename in os.listdir(srcdir):
		# skip dot files like .DS_STORE
		if filename[0] == '.':
			continue	
		srcfile = srcdir + '/' + filename
		(directories, actual_filename) = parse(filename)
		targetdir = dstdir
		for d in directories:
			targetdir += '/'
			targetdir += d
			if not os.path.isdir(targetdir):
				os.mkdir(targetdir)
		dstfile = targetdir + '/' + actual_filename
		logmsg = "moving " + srcfile + " to " + dstfile
		logger.info(logmsg)
		os.rename(srcfile,dstfile)

#
# Main
#

srcdir="/Users/patrick/Desktop/wormhole/"
dstdir="/Users/patrick/Desktop/directory/"
confdir="."
logdir="."

conf_file = "organize.conf"
log_file = "organize.log"
mappings = {}
cycle_time=3

parser = argparse.ArgumentParser(description='Orgainze moves files from a source directory to an index directory. \
The location of the source directory and the destination directory can be controlled by command line switches. \
The program moves files every 30 seconds. The first letter of the file being moved is used to determine which \
index directory inside the destination directory to move the file. For example, the file hive.pdf will be moved \
to a h directory inside the destiation directory. If the h directory does not exist it will be created. \
Placement of files can be controlled by nameing the file to be moved with the [[]] directive. \
A file names [[h]]myfile.pdf would move to file myfile.pdf (the [[h]] is stripped) to the h directory. \
If the string inside [[]] is longer than 1 character the first character is used for file placment. \
Further more, the text inside [[]] is matched against the contents of the configuraiton file which is loaded \
with each move cycle. The configuration file organize.conf has a simple format. Each mapping is on a single line. \
Each mapping consists of two strings sperated by a colon, for example, hive:hadoop. \
If a file is named [[hive]]hive.pdf the file hive.pdf will be saved in the h directory under another sub-directory \
called hadoop. If the configuration was hive:map-reduce the file hive.pdf will be moved to the \
index directory h (contorlled by the h in hive) but placed in a sub-directory map-reduce. \
If the sub-directory map-reduce does not exist it will be created.') 
parser.add_argument('-s','--src',  help='Source directory containing files to move to the destination \
directory hierarchy. Note directories in the sources directory will not be moved', required=False, default=srcdir)
parser.add_argument('-d','--dst',  help='Destination directory. Contains directors a-z which in turn contain the \
moved files organized alphabetically. If specificed files will be in sub-directories of the alphabetical index', required=False, default=dstdir)
parser.add_argument('-c','--conf', help='Configuration directory containing organize.conf', required=False, default=confdir)
parser.add_argument('-l','--log', help='Log directory containing organize.log', required=False, default=logdir)
args = vars(parser.parse_args())

srcdir  = args['src']
dstdir  = args['dst']
confdir = args['conf']
logdir  = args['log']

if not os.path.isdir(logdir):
	print("The log directory (" + dir + ") does not exist, exiting...")
	exit(1)

logger = init_logging()

check = [ ('source', srcdir), ('destination', dstdir), ('configuration', confdir) ]
for (desc, dir) in check:
	if not os.path.isdir(dir):
		logger.error("The " + desc + " directory (" + dir + ") does not exist, exiting...")
		exit(1)

print "Organize.py is running, lets get organized ..."
print "Source directory: " + srcdir
print "Destination directory: " + dstdir
print "Configuration directory: " + confdir
print "Log directory: " + logdir
print

while(1):
	read_config()
	organize()
	time.sleep(cycle_time)

