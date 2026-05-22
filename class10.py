# arg
#def addition(*args):
#    print(args)
#addition(1,2,3,4,5,6)    

#kwargs

#def addition(**kwargs):
#    print(kwargs)
#addition(name="ram",roll_no = 19)

#def addition(*args,**kwargs):
#    print(args)
#    print(kwargs)
    
#addition(1,2,3,4,5,6,name="ram",roll=10)

#recrusive function

#def fact(n):
#    if n ==0 or n ==1:
#        return 1
    
#    return n * fact(n-1)

#final_result=fact(5)

#print("final_result:",final_result)


#def fact(n):
 #   if n == 0 or n == 1:
 #       return n * fact(n-1)
#final_result = fact(5)

#print("final_result:",final_result)



def fact(n):
    if n == 0:
          return 0 
    elif n ==1:
     return 1
    return fact (n-2) + fact(n-1)
for x in range(10):



 print(fact(x),end=" ")




