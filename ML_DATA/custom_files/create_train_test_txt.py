import os
import sys


a = open("train_bottom.txt", "w")
for file in os.listdir("../bottom/train/"):
	if file.endswith('.jpg'):
		a.write("../daten/ML_DATA/bottom/train/"+ str(file) + os.linesep)
		#a.write("../GIT_DATA/ML_DATA/data/data/train/"+ str(file) + os.linesep)

a.close()

b = open("test_bottom.txt", "w")
for file in os.listdir("../bottom/test/"):
	if file.endswith('.jpg'):
		b.write("../daten/ML_DATA/bottom/test/"+ str(file) + os.linesep)
		#b.write("../GIT_DATA/ML_DATA/data/data/test/"+ str(file) + os.linesep)
b.close()

