# from  optparse import  OptionParser
# usage="myprog [-f<filename>][-s<xyz>]arg1[,arg2..]"
# optParser=OptionParser(usage)
# optParser.add_option("-f","--file",action="store",type="string",dest="filename")
# optParser.add_option("-v","--vison",action="store_false",dest="verbose",default="none",help="make losts of noise [default]")
# fakeArgs=['-f',"file.txt",'-v','good luck to you','arg2','arg']
# options,args=optParser.parse_args(fakeArgs)

# print(options.filename)
# print(args)
# print(options.verbose)

import os

def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

print(returnDir())