import os

num = "0123456789"
def renameFiles():
	os.chdir("/Users/fowziya/Downloads/alphabet")
	#grab files

	fileList = os.listdir("/Users/fowziya/Downloads/alphabet")
	#grabfiles for a windos
	#fileList = os.listdir(r"C:\Users\Folder)
	for fileName in fileList:
		print fileName + " " + fileName.translate(None,num)
		os.rename(fileName, fileName.translate(None, num))
		
renameFiles()

#howTo make this program betteR?

#request directory from user and then apply the path they enter to the program
