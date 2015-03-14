import os
for filename in os.listdir("./Source/"):
    info = os.stat(filename)
    print info.st_ctime, filename
