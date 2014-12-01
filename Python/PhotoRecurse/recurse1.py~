import os, time, stat	
#from pathLib import Path 

fpath = "./Source/" 
i = 0 
for root, dirs, files in os.walk(fpath):
    for dir in dirs:
	for file in files:
            if file.endswith(r'.jpg'):
		#print fpath, dir, "/", file
		# newPath = str(fpath) + str(dir) + str("/") + str(file)
		newPath = os.path.join(root, file)
		# print newPath 
		print file, newPath, \
		"created: %s" % time.ctime(os.path.getctime(newPath)), \
		"size: %s" % os.path.getsize(newPath)

		#print stat.ST_CTIME(os.path.getmtime(newPath)) 
		#print time.gmtime(os.path.getmtime(newPath)) 
		#time.gmtime(os.path.getmtime(file)) , #, os.stat(cdate), #, os.stat(file) 
		#time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file)))
		#print PurePosixPath (file) 
		#print dir, "\\", file, time.ctime(os.path.getctime(file))
        	#print file + ",  " + time.ctime("\"" + os.path.getctime(file) + "\"")
        	i += 1
print i
