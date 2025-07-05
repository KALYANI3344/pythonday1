""" conditional statements:in order a block of runin python the conditinal statements divided into "three "types.
1. decision making/conditional statement
2.looping/interative statements
3.jumping/transfer statements

"""
#decision making statements:this statements are used to take the decision and run the program
"""
if
if else
elif
nested if
shorthand if
shorthand if else
"""
#if: the if condition is executed when the condition is "true"
a=5
if a==5:
     print("if condition is executed")
#if else:if the condition in if block is failed then the else block is executed
a="ECE"
if a=="ECE":
     print("the if block is executed")
else:
     print("the else block is executed")          
#elif:when the condition in "if" block failed the elif block is executed
userid=input("enter your user id_...")
password=input("enter your password...")
if userid=="abc12345"and password=="km@12345":
    print("welcome to our netbank of kkkkkbank")
elif userid=="jbj34567" and password=="mk@12345":
    print("welcome to our netbanking of mmmbank")
else:
     print("the userid and password is incorrect try again!!")       
#nestedif
a=10
b=20
c=30
if a==10 and c==30:
    print ("the outer if executed")
    if a==10:
          print("the inner if executed")
    else:  
          print("the outer else executed")
          

