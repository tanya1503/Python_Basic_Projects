#Secret code - Encoding and Decoding

#coding
import random
a=input("Enter the string you want to convert in secret code")
if(len(a)<3):
    b=a[::-1]
    print(b.lower())

else:
    c=a[1::]
    d=c+a[0]
    e=("a","e","i","o","u","z","t")
    i=("b","c","d","e","f","g")
    f=random.choices(e,k=3)
    j=random.choices(i,k=3)
    g=''.join(f)
    l=''.join(j)
    h=g+d+l
   
    print(h.lower())
    




      
      
    
    
