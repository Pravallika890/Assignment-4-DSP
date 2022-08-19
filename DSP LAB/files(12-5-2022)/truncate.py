file=open("pravallika.txt","a")
file.truncate(20)
file.close()


file=("pravallika.txt","r")
print(file.read())
