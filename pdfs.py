import os
intotxt="pdf2txt $1 -o /tmp/my.txt"
print("\033c\033[47;31m\ngive me the file to parse ")
files=input().strip()
os.system(intotxt.replace("$1",files))
f1=open("/tmp/my.txt","r")
a=f1.read()
f1.close()
f=a.find("Alphabetical list of Armv7-M Thumb instructions")
a=a[f:]
f=a.find("A7.7 Alphabetical list of Armv7-M Thumb instructions")
a=a[f:]
f=a.find("System Level Architecture")
a=a[:f]
f1=open("out.txt","w")
f1.write(a)
f1.close()