 

import sys
import os
import hashlib





def comphash(file):

    BUF_SIZE = 65536

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:

         while True:

               data = f.read(BUF_SIZE)

               if not data:

                break

                     sha256.update(data)

    return sha256.hexdigest()


file1 = comphash(sys.argv[1])

file2 = comphash(sys.argv[2])

if file1 == file2:

   print("Both files are same")

else:

   print("Files are different!")
