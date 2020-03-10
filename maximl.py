string=input()
list=[]
count=0
for i in string:
    if i not in list:
        list.append(i)
        count=count+1
print(count)
