#Create a list of all odd numbers between 1 and a max number

n=int(input("Enter the number:"))

list=[]
for i in range(0,n):
    if (i%2==1):
        list.append(i)
        
print(list)