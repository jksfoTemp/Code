import os, time, stat	

fpath = "./Source/" 
i = 0 
for root, dirs, files in os.walk(fpath):
    for dir in dirs:
	for file in files:
            if file.endswith(r'.jpg'):
		newPath = os.path.join(root, file)
		print file, newPath, \
		"created: %s" % time.ctime(os.path.getctime(newPath)), \
		"size: %s" % os.path.getsize(newPath)
        	i += 1
print i
