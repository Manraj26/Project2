print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1. Add product to the cart.")
print("2. Search the product.")
print("3. Delete  the product from the cart.")
print("4. quit.")
x=int(input("Enter your choice :  "))
y=int(input("Enter number of items to be added in the stationary shop :  "))
product={}
while (x!=4):
    c=len(product)
    if(x==1 and c<5):
         for h in range(y):
          a=input("product name:-")
          b=input("product price:-")
          product.update({a:b})
    
    elif (x==3):
         a=input("product name:-")
         product.pop(a)
    elif(c==5):
         print("Cart is full")
    elif(x==2):
         a=input("product name:-")
         t=0
         for i in product:
              if(i==a):
                   print("Product found")
                   t=t+1
              else:
                   t=t
         if (t==1):
              print(" product found")
         else:
              print("ERROR, product not found")
            

         
                           
                   

    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete  the product from the cart.")
    print("4. quit.")
    x=int(input("Enter your choice :  "))
    
    
print(product)   



