#conditional statements
#write a python program to find whether a number is positive or not
num=int(input("enter a number.."))
if num >0:
    print("the number is positive",num)


    #write a program to find biggest of two numbers
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    if a>b:
        print("a is greather:",a)
    else:
        print("b is greather:",b)    

#accept the percentage from the user and display the grade according to the following criteria
pr = int(input("enter your percentage.."))
if pr <=25:
    print("the grade is d..")
elif pr>=25 and pr<=45:
    print("the grade is c..")
elif pr>=45 and pr<=50:
    print("the grade is b..")
elif pr>=50 and pr<=60:
    print("the grade is a..")
elif pr>=60 and pr<=80:
    print("the grade is a+..")
elif pr>=80:
    print("the grade is a++..")
else:
    print("you are fail..")    



    #write a program to display the week names by taking input from user 
    day = int(input("enter your day"))
    if day == 1:
        print("sunday")
    elif day ==2:
        print("monday")
    elif day ==3:
        print("tuesday")
    elif day ==4:
        print("wednesday")
    elif day ==5:
        print("thursday")
    elif day ==6:
        print("friday")
    elif day ==7:
        print("saturday")    
                                            







