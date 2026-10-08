#loops:
#for loop--sequence itteration [list,tapule,strings,dictionary]
#while loop

#forloop
#for variable in sequence:
    #code to be excuted

#emp_data=["vasu","kiran","pavan","ravi","lakshmi"]
#for iteam in emp_data:
    #print(f"{iteam}welcome to python life")


#sample="pythonlife"
#for i in sample:
    #print(f"hello every one")
    #print(f"{i}hello every one")
 
#range() #function /use on for loop
#range(stop)
#range(start,stop)
#range(start,stop,step)

#for i in range(10):#(n-1)/by default 0
   # print(f"{i}")

#for i in range(99,500):
    #print(f"{i}")
#for i in range(0,10,1):#start value by default 0/step value by default 1
    #print(f"{i}")
#for i in range(1,10,2):
    #print(f"{i}")

#for i in range(10,100,5):
    #print(f"{i}")

# i in range(10,50,3):
    #print(f"{i}")

#for i in range(10,50,2):
    #print(f"{i}")

#for i in range(1,11):
    #print(f"2*{i}={i*2}")

#for i in range(1,11):
    #print(f"17*{i}={i*17}")

#table=input("enetr the number: " )
#for i in range(1,11):
    #print(f"{table}*{i}={table*i}")

#nested for loop
#for i in seq:--outer for loop
   # for j in seq:--inner for loop

#for i in range(10):
    #for j in range(5):
        #print(i,j)

#for i in range(1,11):
    #for j in range(1,11):
        #print(f"{i}*{j}={i*j}")
    #print("-"*10)

#while loop----as long as a condition true.(cntrl+c)for interaption
#count=0
##while count>=0:
    #print("welocome to pythonlife")
#count=0
#while count<=3:(False)
    #print(count)
    #count+=1

"""while True:
    user_name= input("eneter user name:  ")
    password= input("enter password:  ")
    if user_name == "vijay" and password == "vijay@123":
       print(f"login success..")
       print(f"welcome{user_name}")
       break
    else:
        print(f"invalid login credentials")"""

"""while True:
    grade_marks=int(input("enter marks....."))
    if grade_marks<0 or grade_marks>100:
         print(f"please enter marks betwen 0-100")
    elif grade_marks>=80:
         print(f"you got pass{grade_marks}.you are grade is A")
    elif grade_marks>=50:
         print(F"you got pass{grade_marks}.you  are grade is B")
    elif grade_marks>=35:
         print(f"you got pass{grade_marks}.you are grade is C")
         break
    else:
         print(f"your failed....")"""

#nested while:
#while cond:outer file 
    #while cond:#inner while

"""while True:
    print("welcome to python life")
    print("hello everyonen...")
    while True:
        print("inner while loop")
        print("hi everyone welocome to pythonlife.....")
        break
    break"""

"""num=0
while num>=0:
    sum=(input("enter number...."))
    print(f"evennumber")
    break"""

"""while True:
    user_name=(input("enter usernsme:  "))
    print(user_name)
    if user_name == "stop":
       break"""