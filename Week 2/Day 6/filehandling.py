# File Handling
# write method (W mode)
File=open("Hello.txt",'w')
File.write("Hello World")
File.close()

# Read method(R mode)
rFile=open("Hello.txt",'r')
print(rFile.read())
rFile.close()

# Append method(A mode)
aFile=open("Hello.txt",'a')
aFile.write("\nHello using append method")
aFile.close()


# For Remove file from os we have to import os library

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("Removed Successfully")
else:
    print("File Does Not Exist!")


    