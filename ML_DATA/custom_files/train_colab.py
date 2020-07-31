import os
import sys

#person


a = open("train_person.txt", "w")
for file in os.listdir("/content/MyDrive/data/persona/"):
	if file.endswith('.jpg'):
		a.write("/content/MyDrive/data/persona/"+ str(file) + os.linesep)

a.close()


#b = open("test_person.txt", "w")
#for file in os.listdir("/content/MyDrive/data/persona/"):
#	if file.endswith('.jpg'):
#		b.write("/content/MyDrive/data/persona/"+ str(file) + os.linesep)
#b.close()

