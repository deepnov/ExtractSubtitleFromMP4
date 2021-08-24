import os
import sys
import io

def listfiles(scriptparam,depth):
    dirList = os.listdir()
    for filename in dirList:
        x=0
        holder=""
        for x in range (0,depth):
            holder=holder+"\t"
        if(depth>0):
            holder = holder + "->" + filename
        else:
            holder=holder+filename
        #print(depth) #was used for troubleshooting depth of subfiles/folders
        if filename.endswith(".mp4"):
            print(filename+"\n")
            os.system('ffmpeg -hide_banner -i "'+filename+'" -map 0:s:0 "'+filename+'".srt')#ffmpeg tool should be installed in the machine before running this tool


        if (filename != scriptparam):
            
            if os.path.isdir(filename):
                #print(filename + " is a folder") #was used from troubleshooting if file was a folder or file
                os.chdir(filename)
                depth=depth+1
                listfiles(scriptparam, depth)
                depth=depth-1
                os.chdir("..")


location=os.getcwd()
location=location+'\\'
os.chdir(location)
print(location)
listfiles(location,0)
