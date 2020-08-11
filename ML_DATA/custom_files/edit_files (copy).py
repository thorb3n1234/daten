import glob,os,shutil
import cv2 as cv
counter =1
files = sorted(glob.iglob(os.path.join("../con_and_bot/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size != 0 and str(file) != "../con_and_bot/classes.txt":
			counter = counter + 1 
			f = open(file,"r")
			print(file)
			content = f.readlines()
			f = open(file,"w")
			for part in content:
				splits = part.split(" ")
				#part[0] = 0
				newstr = "1" + part[1:-1] + "\n"
				print(newstr)
				f.write(newstr)
print(str(counter))
