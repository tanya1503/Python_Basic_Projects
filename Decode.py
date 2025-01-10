#Decode the code

x=input("Enter the word you want to decode")
if len(x)<3:
    b=x[::-1]
    print(b.lower())
    
else:
    c=x[3::]
    d=c[:-3]
    e=d[2]+d[0]+d[1]
    print(e)
    
 