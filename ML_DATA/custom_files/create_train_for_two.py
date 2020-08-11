import os
import sys

#CONNECTION
a = open("con_and_bot_train.txt", "w")
for file in os.listdir("../con_and_bot/train/"):
	if file.endswith('.jpg'):
		a.write("../daten/ML_DATA/con_and_bot/train/"+ str(file) + os.linesep)

a.close()


b = open("con_and_bot_test.txt", "w")
for file in os.listdir("../con_and_bot/test/"):
	if file.endswith('.jpg'):
		b.write("../daten/ML_DATA/con_and_bot/test/"+ str(file) + os.linesep)
b.close()

c = open("con_and_bot_valid.txt", "w")
for file in os.listdir("../con_and_bot/valid/"):
	if file.endswith('.jpg'):
		c.write("../daten/ML_DATA/con_and_bot/valid/"+ str(file) + os.linesep)
c.close()
