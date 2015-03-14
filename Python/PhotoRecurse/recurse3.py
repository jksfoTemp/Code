import os, time, stat, sys, argparse 

#def main(argv):
fpath = "./Level10/"
i = 0
    #print "Hello"
    #parser = argparse.ArgumentParser()
    #parser.add_argument("ParentDir")
    #args = parser.parse_args()
    #print args.echo

    #try:
    #opts, args = getopt.getopt(argv, [])
    #except getopt.GetoptError as err:
    #    print str(err)
    #    sys.exit(2)

    #    print 'Argument List:', str(sys.argv)

for root, dirs, files in os.walk(fpath):
    for dir in dirs:
        for file in files:
            if file.endswith(r'.jpg'):
                newPath = os.path.join(root, file)
                print (file, newPath,\
                "created: %s" % time.ctime(os.path.getctime(newPath)),\
                "size: %s" % os.path.getsize(newPath))
        i += 1
    print(i)
