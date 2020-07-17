import os
import sys

#CONNECTION
a = open("train.txt", "w")
for file in os.listdir("../data/data/train/"):
	if file.endswith('.jpg'):
		a.write("../daten/ML_DATA/data/data/train/"+ str(file) + os.linesep)

a.close()


b = open("test.txt", "w")
for file in os.listdir("../data/data/test/"):
	if file.endswith('.jpg'):
		b.write("../daten/ML_DATA/data/data/test/"+ str(file) + os.linesep)
b.close()



#BOTTOM


a = open("train_bottom.txt", "w")
for file in os.listdir("../bottom/train/"):
	if file.endswith('.jpg'):
		a.write("../daten/ML_DATA/bottom/train/"+ str(file) + os.linesep)

a.close()


b = open("test_bottom.txt", "w")
for file in os.listdir("../bottom/test/"):
	if file.endswith('.jpg'):
		b.write("../daten/ML_DATA/bottom/test/"+ str(file) + os.linesep)
b.close()
