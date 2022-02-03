a=input("What is the path of the first file?,\n")
b=input("What is the path of the second file?,\n")

c1=open(a)
readc1=c1.read()
c2=open(b)
readc2=c2.read()

c1=open(a,"w")
c1.write(readc2)
c2=open(b,"w")
c2.write(readc1)