import os, time, stat, sys, argparse 

fPath = ''
i = 0
parser = argparse.ArgumentParser()
print('Begin')
try:
    parser.add_argument('path')
    args = parser.parse_args()
    #print(args.path)
    fPath = args.path
    for root, dirs, files in os.walk(fPath):
        print(root)
        for dir in dirs:
            print(dir)
            for file in files:
                if file.endswith(r'.jpg'):
                    newPath = os.path.join(root, file)
                    print (file, newPath,\
                    'created: %s' % time.ctime(os.path.getctime(newPath)),\
                    'size: %s' % os.path.getsize(newPath))
            i += 1
        print(i)
except:
    print ('Err: ', sys.exc_info()[0])
if (i==0):
    print('No files found in input directory')
print('Done')
