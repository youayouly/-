n=int(input())
#vk相邻
ket_str=str(input())

num=k=0
for i in range(len(ket_str)-1):
    
    if ket_str[i]=='V' and ket_str[i+1]=='K':
        num+=1
    

    if(k==0):
        if ket_str[i]==ket_str[i+1]:
          num+=1
          k+=1
        
print(num)