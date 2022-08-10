import zipfile

myZip = zipfile.ZipFile("file_zip.zip","w")

myZip.write("example1.txt")
myZip.write("example2.txt")

myZip.close()