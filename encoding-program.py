import chardet
import urllib.request
import codecs

file = input("enter name of the file: ")            # for getting the file name from the user
with open(file, 'rb') as f:                         # opening the file entered by user in read-binary mode so that strings can be encoded
    data = f.read()                                 # reading the contents of th file
    det = chardet.detect(data)['encoding']          # detecting encoding of the file
    print(det)

# library used to read contents of a web page in web browser. This is a way for reading web page content and detecting encoding in
# web browser
rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()      
print(chardet.detect(rawdata))

# Converting file to utf encoding 

print("Conveting it into utf-8 encoding...")
target = input("give a name to your target file: ")
with codecs.open(file, "r") as sourceFile:
    with codecs.open(target, "w", "utf-8") as targetFile:
        contents = sourceFile.read()
        result = targetFile.write(contents)
        print(result)
