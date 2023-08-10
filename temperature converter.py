temp=input("input the temperature you like to convert : ")
degree=int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result=int(round((9*degree)/+32))
    o_convention = "Fahrenheit"

elif i_convention.upper()  == "F":
    result=int(round((degree-32)*5/9))
    o_convention = "Celsius"

else:
    print("input proper convention") 
    exit()   

print("the temperaturein" ,o_convention, "is",result, "degrees.")    
