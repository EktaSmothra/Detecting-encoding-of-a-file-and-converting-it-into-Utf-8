import chardet
import urllib.request
import codecs

file = input("enter name of the file: ")
with open(file, 'rb') as f:
    data = f.read()
    det = chardet.detect(data)['encoding']
    print(det)

rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
print(chardet.detect(rawdata))

print("Conveting it into utf-8 encoding...")
target = input("give a name to your target file: ")
with codecs.open(file, "r") as sourceFile:
    with codecs.open(target, "w", "utf-8") as targetFile:
        contents = sourceFile.read()
        result = targetFile.write(contents)
        print(result)
