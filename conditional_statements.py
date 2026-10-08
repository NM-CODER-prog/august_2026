#Controlstatements 3 types  [1st--conditional statemets] [2nd--looping statements] [3rd--Transfer statements]
#1st conditional statemnts--->flow of execution and decision making 
#if----if condition true block code will executed and if condition false then block of code is skipped.
"""syntax:
if condition:
    statement 1
    statement 2
    statement n   [front space is called indentation]"""
#elif
#else
#nested statements
#shorthand if else statements

#if
age=35
if age>=18:
    print(f"you are eligible to vote age {age}")


_name="ajay"
_height =5.7
if _name =="ajay" or _height ==5:
    print(f"welome{_name}")

_name=15
if _name<=25:
   print(not(_name))



#else
#else provide alternatove block of code/when if statements executes condition false
"""syntax:
if
   block of code execute if condition is True
else:
   block of code execute if condition is False"""

user_name="vijay"
password="vijay@123"
if user_name=="vijay" and password=="vijay@123":
    print(f"login success..")
    print(f"welcome{user_name}")
else:
    print(f"invalid login credentials")

product_name="computertable"
product_coast= 3000
if product_name=="computertable" or product_coast<=2000:
    print(f"{product_name} deliverd with good price{product_coast}")
else:
    print(f"{product_name} delivred not good price{product_coast}")

#elif--->check multiple conditions one after another/for tricky decisions

"""syntax:
if   condition-1:
      statement 1
elif condition-2:
     statement 2
elif condition-3:
     stetement 3
else:
     statement"""

#one method
grade_marks=100
grade_marks=(int(input("enter marks...")))
if grade_marks>=80 and grade_marks<=100:
    print(f"congragulations your pass.you are grade is A")
elif grade_marks>=50 and grade_marks<=80:
    print(f"congragulations your pass.you are grade iS B")
elif grade_marks>=35 and grade_marks<=50:
    print(f"congragulations your pass")
elif grade_marks>=0 and grade_marks<=35:
    print(f" your failed")
else:
    print(f"enter marks between 0-100")


#2nd method
grade_marks=int(input("enter marks....."))
if grade_marks<0 or grade_marks>100:
    print(f"please enter marks betwen 0-100")
elif grade_marks>=80:
    print(f"you got pass{grade_marks}.you are grade is A")
elif grade_marks>=50:
    print(F"you got pass{grade_marks}.you  are grade is B")
elif grade_marks>=35:
    print(f"you got pass{grade_marks}.you are grade is C")
else:
    print(f"your failed....")


#nested if-else/use for series of decisions/it allows for more complex condotional logic/indentation is the only way to differentiate the level of nesting..

"""syntax:
if conditional:
     code block for condition1
    if condition2:
      code block for condition2
    else:
        code block for condition2 being False
else:
    code block for conditional being False"""

user_name=input("enter the username..")
password=input("enter password")
if user_name=="satya":
    if password=="satya@123":
        print(f"login success..")
        print(f"welcome{user_name}")
    else:
        print(f"invalid password")
else:
    print("invalid username...")


amazon_products=["tops","jeans","kurthis","menkurthis","sarees,dress",["cosmetics","makeupproducts"],("kidswear","footwear")]
product_prices=[500,1000,1000,1500,2000,1000,5000,4000]
amazon_products=input("enter product...")
product_prices=int(input("enter price...."))
if amazon_products in ["tops","jeans","kurthis","menkurthis","sarees,dress",["cosmetics","makeupproducts"],("kidswear","footwear")] or product_prices in [500,1000,1000,1500,2000,1000,5000,4000]:
   if   amazon_products in ["tops","kurthis","sarees,"]:
        product_prices in  [500,1000,1000,1500,2000,1000,5000,4000]
        print(f"women wear avilable")
else:
    print(f"women wear not avilable")
    if  amazon_products==["jeans","menskurthis"]:
            product_prices==[1000,1000]
            print(f"mens kurthis are avilable")
    else:
        print(f"mens wear not available")
        if amazon_products==["cosmetics","makeupproducrs"]:
             product_prices==[5000]
             print(f"makeup product avilable")
        else:
            print(f"makeup produccts not avilable")
            if amazon_products==["kidswear","footwear"]:
                  product_prices==[4000]
                  print(f"kids wear avilable")
            else:
                   print(f"kids wear not available")
                
     
#short hand statement:
# if ,else,if-else
    
#syntax:
#result=value_if_true if condition else value_if_false
 #ex:
num_1=int(input("enter number..."))
result="even number"if num_1%2==0 else"not even"
print(f"result")

num_1=int(input("enter number..."))
print("even number")if num_1%2==0 else print("not even")















    



























 








