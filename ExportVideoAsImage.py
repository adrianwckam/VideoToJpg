import cv2
import glob
import os 
from datetime import datetime
dir = "/video processor/"
FileList = glob.glob(dir+"input/*.mp4")
timer = datetime.now()
print(str(len(FileList))+" File was found") 
if not os.path.exists(dir+"outputs/"):
    os.makedirs(dir+"outputs/")
for i in FileList:
    if not os.path.exists(dir+"outputs/"+os.path.basename(i)):
        os.makedirs(dir+"outputs/"+os.path.basename(i))
    vidcap = cv2.VideoCapture(i)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(dir+"outputs/"+os.path.basename(i)+"/frame%d.jpg" % count, image)      
        success,image = vidcap.read()
        print('Frame: ', count)
        count += 1
print("Task completed")
print("Process took: "+str(datetime.now()-timer)+"seconds")
input("Press enter to end process")