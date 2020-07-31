import glob,os,shutil
import cv2 as cv
counter =0
files = sorted(glob.iglob(os.path.join("/content/MyDrive/data/persona/","*.*")))

for file in files:
	counter = counter + 1 
print(str(counter))
