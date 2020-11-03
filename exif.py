import exiftool
import os
 
def getm(fname,metadata):
    with exiftool.ExifTool() as et:
        metadata=et.get_metadata(fname)
    print (metadata)
    for dat in metadata.keys():
        if dat=='ExifTool:ExifToolVersion':
            print (metadata[dat])
    return metadata
print(os.getcwd())
os.chdir('/Users/Jim/Desktop')
print('You are now running under: ',os.getcwd())
file_name=str(input('Input exact file name under'+os.getcwd()+':'))
md=''
a=getm(file_name,md);
print(a)
