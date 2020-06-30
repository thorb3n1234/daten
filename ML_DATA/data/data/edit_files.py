import glob,os,shutil
counter =1
files = sorted(glob.iglob(os.path.join("train/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size != 0 and str(file) != "train/classes.txt":
			counter = counter + 1 
			f = open(file,"r")
			content = f.readline()
			parts = content.split()	
			if len(parts[0]) > 1:		
				f = open(file,"w")
				rest_str = parts[1:]
				startstr = '0 ' + str(parts[0][1:]) + ' '
				newstr = startstr
				for i in parts[1:]:	
					newstr = newstr + i + ' '
				print(newstr)
				f.write(newstr)
			f.close()
print(str(counter))
