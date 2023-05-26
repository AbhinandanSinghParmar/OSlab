a=int(input("No of inputs"))
list=[]
for i in range(a):
    num=int(input("Enter Number"))
    list+=[num]
print("original list is ",list)
for i in range(len(list)):
    for j in range(i + 1, len(list)):

        if list[i] > list[j]:
           list[i], list[j] = list[j], list[i]

print (list)
