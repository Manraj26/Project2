a={}
b=input("Product name or enter 0 to stop:-")
while(b!="0"):
    c=input("product price:-")
    a.update({b:c})
    if(len(a)==5):
        break
    b=input("Product name or enter 0 to stop:-")


print(a)    


