import os
file1=input("input file 1 name:")
file 2=input("input file2 name:")
os.rename(file2,"temp")
os.rename(file1,file2)
os.rename("temp",file1)
