"""
#write a program to accept two from the user and an operator and perform operation accordingly
num1:5
num2:10
opr:+
answer:15
"""
num1 =int(input("enter a number.."))
num2 =int(input("enter a number.."))
opr = input("enter a operator:")
if opr=="+":
    print("the answer:",num1+num2)
elif opr=="-":
    print("the answer:",num1-num2)
elif opr=="*":
    print("the answer:",num1*num2)
elif opr=="/":
    print("the answer..",num1/num2)
else:
    print("wrong operatorselected..")    


 
#write a program to accept a number from 1to 12 and display the months like jan and days of the months
mon_num=int(input("enter the month number 1 to 12.."))
if   mon_num==1:
    print("the month is jan it has 31days..")
elif mon_num==2:
    print("the month is feb it has 28 days..")
elif mon_num==3:
    print("the month is march it has 31days..")
elif mon_num==4:
    print("the month is april it has30 days..")
elif mon_num==5:
    print("the month is may it has  31days..")
elif mon_num==6:
    print("the month is june it has 30days..")
elif mon_num==7:
    print("the month is july it has 31days..")
elif mon_num==8:
    print("the month is august it has 31days..")
elif mon_num==9:
    print("the month is september it has 30days..")
elif mon_num==10:
    print("the month is october it has 31 days..")
elif mon_num==11:
    print("the month is november it has 30days.")
elif mon_num==12:
    print("the month is december it has 31days..")


#write a program to display "hello" if a number entered by user is a multiple of five otherwise print "bye
num= int(input("enter a number.."))
if num%5==0:
    print("hello")
else:
    print("bye")    









    
       









            
