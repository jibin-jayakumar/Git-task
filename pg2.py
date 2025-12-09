print("Comparison & Calculation :")
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
if(num1>num2):
    print("Comparison:")
    print( "Number 1 is greater:",num1,">",num2)
    print("CALCULATION:")
    print("Adding 10 ")
    x= num1+10
    print("Updated first number")
    print("10 +",num1,"=",x)
   
else:
        print("Comparison:")
        print( "Number 1 is lesser:",num1,"<",num2)
        print("CALCULATION:")
        print( "Substracting 5")
        y= 5-num1
        print("Updated fisrt number")
        print("5 -",num1,"=",y)
