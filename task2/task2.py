import sys
file_name1=sys.argv[1]
file_name2=sys.argv[2]
file1=open(file_name1)
t1=file1.read()
file1.close()

file2=open(file_name2)
mas2=[]
for i in file2:
    mas2.append(i.split())
file2.close()

mas1=list(t1.split())
mas1[:]=map(float,mas1)

for i in range(len(mas2)):
    d=0
    s=(mas1[0]-float(mas2[i][d]))**2+(mas1[1]-float(mas2[i][d+1]))**2
    if s<mas1[2]**2:
        print(1,end=' ')
    elif s==mas1[2]**2:
        print(0,end=' ')
    elif s>mas1[2]**2:
        print(2,end=' ')
    
     

    


    







