p_color1=input("Enter Color (Red, Blue and Yellow):")       
q_color2=input("Enter Color (Red, Blue and Yellow):")  



if(p_color1=="Red" and q_color2=="Blue"):
    print("Red+Blue=Purple")
elif(p_color1=="Red" and q_color2=="Yellow"):
    print("Red+Yellow=Orange")
elif(p_color1=="Blue" and q_color2=="Red"):
    print("Blue+Red=Purple")     
elif(p_color1=="Blue" and q_color2=="Yellow"):
    print("Blue+Yellow=Green") 
elif(p_color1=="Yellow" and q_color2=="Red"):
    print("Yellow+RED=Orange")
elif(p_color1=="Yellow" and q_color2=="Blue"):
    print("Yellow+Blue=Green")

else:
    print("COLOR ERROR")