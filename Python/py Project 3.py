salary=int(input("Enter salary:"))
country=str.lower(input("Enter Country Name:"))
def ConvertSalary(salary,country):
    if(country=="canada"):
        Total_Salary_convert=salary*0.5
        return Total_Salary_convert
    elif(country=="us"):
        Total_Salary_convert=salary*0.75
        return Total_Salary_convert
    elif(country=="combodia"):
        Total_Salary_convert=salary*40
        return Total_Salary_convert
    elif(country=="uk"):
        Total_Salary_convert=salary*1.5
        return Total_Salary_convert
    else:
        return 0
        
Total_Salary_convert=ConvertSalary(salary,country)   

if(country=="canada"):
    if(Total_Salary_convert>30000 and country=="canada"):
        print("You are rich at Canada")
    else:
        print("You are below poverty line") 
elif(country=="us"):
    if(Total_Salary_convert>35000 and country=="us"):
        print("You are rich at US")
    else:
        print("you are below poverty line")
elif(country=="cambodia"):
    if(Total_Salary_convert>150000 and country=="cambodia"):
        print("You are rich at Cambodia")
    else:
        print("you are below poverty line")
elif(country=="uk"):
    if(Total_Salary_convert>45000 and country=="uk"):
        print("you are rich at UK")
    else:
        print("You are below poverty line")
else:
    print("Error")