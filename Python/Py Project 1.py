p_month=int(input("Enter Month:"))
q_day=int(input("Enter Day:"))
r_year=int(input("Enter year:"))
date_check=True



if(p_month>0 and p_month<13):
    date_check=True
else:
    date_check=False
    print("Month cannot be more than 12 and less than 1")    



if(q_day>0 and q_day<32):
    date_check=True
else:
    date_check=False
    print("DAY ERROR")



if(r_year>0 and r_year<99):
    date_check=True
else:
    date_check=False
    print("Year cannot be more than 99 and less than 1")   




if(date_check):
    print(p_month,"/",q_day,"/",r_year)
else:
    print("ERROR")      
