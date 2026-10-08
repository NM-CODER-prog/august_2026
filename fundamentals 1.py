#print(exp)-->it used to display the information on the screen.
print(10+10)
print(10*2)
print(20/2)


#comment's
#Single line comment
#double line comment
#triple line comment

num1=10
num2=20
sum=num1+num2
print(sum)


  #above code is used to perform addition operation
  #num1=10is variable it contains a value of 10
  #num2=20 is variable it contains a value of 20 
  #later next line performed addition operation by using + operator 
  #and result hasbeen displayed on the screen by using print satatement(print function)

#variables creation rules.
#syntax of variable
#variable=value
# variable is assigenment operators variable is used to store the data in the memory location
#age(variable)=(20)(value) data type of variable is integer

age=50
print(age)

Product_cost=1000
print(Product_cost)

nyka_bill=3000(int)
print(nyka_bill) 

client_name=("Nandini")#string
print(client_name)

marks_percentage=75.5  #float
print(marks_percentage)

humans_natureisgood=True
print(humans_natureisgood)

Student_id=2348
print(Student_id)
print(id(Student_id))#[every time give different memory location for the same variable]

#Variable name start with letter or underscore(_) and it should not start with number or special character(A-Z, a-z,0-9,_).
# Variable name  are case senstive.
#VarIable name should not be a Keyword.

_Person_name="naveen"
print(_Person_name)

NANI_nickname="nani"
print(NANI_nickname)

#10_value=70     [invalid creation of variable name because it doesn't start with number]
#print(10_value)

Principale_id_1=445678
print(Principale_id_1)
print(id(Principale_id_1)) # [memory allocaion we can defined by using id() function. every time give a diffrent memory location for the same variable]
#[reserved keywords we cannot use as a variable names like def,if,else,for,while,break,continue,return extra...]


#Variable cases's topic's

#Camelcase--> C++,Java
#studentName="kiran"
#print(studentName)

#snakecase--->Python
#student_name="kiran"
#print(student_name)

#pascal case-c++,Java
#StudentName="kiran"
#print(StudentName)

#Datatypes
#int
#float
#complex
#strings
#list 
#tuple
#set
#dictionary
#booleam
#None
#frozenset

#int
num_1=30
print(num_1)
print(type(num_1))
print(id(num_1))
print(float(num_1))
print(str(num_1))
print(complex(num_1))

sum_1=-20
print(sum_1)
print(type(sum_1))
print(id(sum_1))
print(float(sum_1))
print(str(sum_1))
print(complex(sum_1))

product_offer=00
print(product_offer)
print(type(product_offer))
print(id(product_offer))
print(float(product_offer))
print(str(product_offer))
print(complex(product_offer))


#float
height=5.6
print(height)
print(type(height))
print(id(height))
print(int(height))
print(str(height))
print(complex(height))

#str/a-z,0-9,special characters--it is used to represent sequence of characters ,and it is used to store textual information/

scentence='welcome to python life'
print(scentence)
print(type(scentence))
scentence="welcome to python world"
print(scentence)
print(type(scentence))
scentence="hellow orld"
print(scentence)
print(type(scentence))

navya_id="navyam2681@gmail.com"
print(navya_id)
print(type(navya_id))

wakeup_time="6'0'clock"
print(wakeup_time)
print(type(wakeup_time))

product="20,000"
print(product)
print(type(product))

#type conversion--> 1.implict type converstion(automatic) 2.explicit type converstion(manual)

#int--->float
product_coast=15500
print(product_coast)
print(type(product_coast))
_sample=float(product_coast)
print(_sample)
print(type(_sample))

height=5.7
print(height)
print(type(height))
_data=(int(height))
print(_data)
print(type(_data))


nykaproducts_coast=2000
print(nykaproducts_coast)
print(type(nykaproducts_coast))
price_1=float(nykaproducts_coast)
print(price_1)
print(type(price_1))

#str--->int[only numbers convert to int]
user_data="12345"
print(type(user_data))
num_1=int(user_data)
print(num_1)
print(type(num_1))

name="vasu@123"
print(type(name))

#input---->used to enter inputs dynamecally

num_1=input("enter the number: ") #str[input function by defaul read string]
num_2=input("enter the number: ")#str
_sum=num_1+num_2 #str concatination
print(_sum)


num_1=int(input("enter the number: "))# converstion to int
num_2=int(input("enter the number: "))
result=num_1+num_2
print(result)

num_1=10 #mplict type converstion
num_2=5.7
sum=num_1+num_2
print(sum)

#Mutable data types
#list
#set
#Dictionary

#immputable data types
#numerics
#tuples
#strings


#List--->
#mutable
#define using []
 
sample_list=[35,5.7,"pythonlife"]#elements,mutable,we can add values
print(sample_list)#order sequence of elements
print(type(sample_list))
print(id(sample_list))
sample_list.append(45.57) #add valu
print(sample_list)
print(id(sample_list))

insurences_details=[5.7,120,5000,"srinivas",(1,2,3),[2,3,4]]# list carry list element and tuple element calling nested list
print(insurences_details)
print(type(insurences_details))
print(id(insurences_details))
insurences_details.append("naveen")#append only one element add only oen valu not multiple
print(insurences_details)
print(id(insurences_details))#print same order




#tuple
sample_tuple=(123,5498,48,"pythonlife",[1,2,3],(4,5))#print same order and tuple carry list and tuple  calling nested tuple
print(sample_tuple)
print(type(sample_tuple))
sample_tuple.append(10)
#not append value or element because immutable
#contains all type of data like numeric ,alphanumericslike adhar data,pan card data,passport data,accountnumber

#set
#unorderd collection of unique elements
#defined with {} and camma separated
  
sample_set={"pythonlife",68789,5,77,(45,"sample","pythonlife"),45,45,45,45,45,}#print unordererd & dublecates elments show one 
print(sample_set)#not contain immutable not contain set.
#Dictonaries
# collection of key=value pairs
#key must ne unique
#defined {}
#keys contains immutable data types like string ,numbers,tuples

sample_dictonary={1:"vasu",2:"kiran",3:"ravi",4:"raju",}#define same order
print(sample_dictonary)
print(type(sample_dictonary))
print(id(sample_dictonary))

sample_dictonary={"user1":"user1@123","user2":"user2@123","user3":"user3@123","user4":"user4@123",1:(1,2,3),7:{7,8,9},3:456,(5,6,7):10}
print(sample_dictonary)

sample_dictonary={"user1":"user1@123","user1":"user2@123"} #if key are same replaced by new value
print(sample_dictonary)

#complex datatype
#in python ,a complex data type used to represent complex number. A complex number consists of a real part and an imaginary part,and its written in the form a+bj
num_1=5+10j #you cant change real or imaginary parts directly.and immutable data type
print(num_1)
print(type(num_1))
print(id(num_1))

voltage=230+50j
current=10+2j
print(voltage+current)

#bolean data type-->Frue valuse and True values True consider 1 and False consider 0

Sample_boolean=True
print(Sample_boolean)

Sample_boolean=False
print(Sample_boolean)


num_1=1
num_2=0
print(num_1+num_2)


#datatype converstion

#list -->set

sample_dataset=["ravi","raju","rajesh","rajesh","ramya",120,5.7,True]
print(sample_dataset)
sample1=(set(sample_dataset))
print(sample1)
sample2=(list(sample1))
print(sample2)


#list-->tuple

sample_dataset=["ravi",5.7,150,"raju","raju",[1,5,3],(1,2,3)]
print(sample_dataset)
sample1=(tuple(sample_dataset))
print(sample1)

#tuple-->set-list  element not spported in type converstion 

sample_dataset=("ravi","ravi","raju",5.7,(1,2,3),123)
print(sample_dataset)
sample1=(set(sample_dataset))
print(sample1)

#set-->list
sample_dataset={"raju","raju",5.7,143,(12,34,56)}
print(sample_dataset)
sample1=(list(sample_dataset))
print(sample1)












































 






















































