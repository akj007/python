file=open("demo.txt","w")

file.write("Hello World\n")

file.write("This is a new text file")

file.close()

file=open("demo.txt","r")
filec=file.read()
print(filec)
file.close()
