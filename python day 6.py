#express delivery
weight=int(input("enter the weight.."))
if weight==4:
    print("the delivery can be expected within 24hrs..")
    if weight<=10:
        print("need to pay an extra amount for extra weight..")
    else:
        print("no need to pay an extra charge have a great delivery!!")
else:
    print("need to wait 3-5 business days to expect the delivery") 


#lopping statements:
# looping statements and also called as interative statements
# these statements are used to run a particular condition 
# no of times...the brotely divided into two types
# 1.while loop
# 2.for loop  
# """
# #while: it executed when the condition is true
# """
# syntax: while condition :
# statements
# exit condition/incrementation
    
i=1
while i<=10:
    print(i)



    #eg1:
    i=1
    while i<=10:
        #print(i)--> in this particular line the 
        #"i"value runs "n" terms because no incrementation/exit code specification
        print("the value",i)
        i+=1


    #eg2:
    while True:
        print("the while condition") 
#     



    #note: As default condition is true the while loop runs "infinite times"
    #eg3:
    while false:
        print("the while condition")





        #jumping /transfer statements:
        #these statements are used to cannot the normal
        # execution of a program they are of two types
        # 1.break:this statements is used to terminate/break the loop
        # 2.continue:this statements are used to skip current iteration and run the next iteration

        i=1
        while i<=10:
            i +=1
            if i==6:
                break#terminals/stops the program
            print(i)


        i=0
        while i<=10:
            i+=1
            if i==6:
                continue#skips the current iteration
            print(i)



                
         


    
   
       






 
     

