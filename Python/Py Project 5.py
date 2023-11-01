print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
print("1. Add a record..")
print("2. Search a record..")
print("3. Change a record..")
print("4. Delete a record..")
print("5. Quit..")
phoneDirectory={}
p=int(input("Enter your choice:- "))
while (p!=5):
    if (p==1):
        s=input("ENTER NAME:- ")
        t=input("ENTER YOUR 10-DIGIT PHONE NUMBER:- ")
        if len(t)==10:
            
         phoneDirectory.update({s:t})
         print("RECORD ADDED..")
        else:
            print("enter 10 digits only..") 
    elif (p==2):
        a=input("Enter name to search:- ")
        u=0
        for i in phoneDirectory:
            if (i==a):
                print("Found..")
                u=u+1
            else:

                u=u
                
        if (u==1):
            print({a:t})
        else:
            print("It is not in this directory..")
    elif (p==3):
        print(phoneDirectory)
        print("CHOOSE NAME FROM DIRECTORY TO CHANGE..")
        b=input("Enter name to update:- ")
        if(b==s):
          c=input("Enter new 10-digit phone number:- ")
          if len(c)==10:
           phoneDirectory.update({b:c})
           print("RECORD UPDATED..")
          else:
              print("enter 10 digits only..")
        else:
            print("PUT VALID INPUT..")
          
    elif (p==4):
        d=input("Enter name to delete:- ")
        if (d==s):
            phoneDirectory.pop(d)
            print("RECORD DELETED..")
        else:
            print("Choose from the directory..")
    else:
        print("CHOOSE INPUT FROM THE MENU..")    

    print("1. Add a record..")
    print("2. Search a record..")
    print("3. Change a record..")
    print("4. Delete a record..")
    print("5. Quit..")
    p=int(input("Enter your choice:- "))
print(phoneDirectory)        
