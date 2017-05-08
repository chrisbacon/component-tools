import os
import sys
import glob

working_path = os.path.dirname(os.path.realpath(__file__))

old_name = sys.argv[1]
new_name = sys.argv[2]

old_name_normalized = old_name.lower()


if glob.glob(os.path.join(working_path, old_name) + '.component.*'):
	for filename in os.listdir(working_path):
		if filename.startswith(old_name):
			newfilename = new_name + filename[len(old_name):]
			old_path = os.path.join(working_path, filename)
			new_path = os.path.join(working_path, newfilename)
			os.rename(old_path, new_path)
else:
	print 'no filename containing ' + old_name + '.component found in path ' + working_path






