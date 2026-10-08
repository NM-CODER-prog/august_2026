#python operators

#Arithmetic operators
"""addition(+)
subraction(-)
multiplecation(*)
division(/)
modulus(%)
floor divison(//)
exponentiation(**)"""

#symbol or keyword that perform an operation on one or more operandas

num_1=10
num_2=5
result=num_1+num_2
print(result)

print(f"num_1{10}\n num_2={5} \nfinalresult {15}\n")

num_1=20
num_2=10
result=num_1-num_2
print(result)

num_1=10
num_2=2
result=num_1*num_2
print(result)

num_1=10
num_2=5
result=num_1/num_2
print(result)

num_1=10
num_2=3
result=num_1//num_2
print(result)

num_1=10
num_2=2
result=num_1%num_2
print(result)

num_1=10
num_2=2
result=num_1**num_2
print(result)

a=10
b=5
result=(a+b)**2
print(result)

#Assigment oparetors
#operation and assuginment both can do

num_1=10
num_1+=5
print(num_1)

num_2=10
num_2-=5
print(num_2)

num_3=5
num_3*=5
print(num_3)

num_4=2
num_4**=2
print(num_4)

num_5=10
num_5/=2
print(num_5)

num_6=100
num_6//=10
print(num_6)

num_7=20
num_7%=10
print(num_7)

#Comparistion operators
"""==
/=
<=
>=
<
> after comparision will get boolean [True , False]"""

product_coast1=1000
product_coast2=900
print(product_coast1==product_coast2)

name_id1=1234
name_id2=1235
print(name_id1>name_id2)
print(name_id1<name_id2)

result_1=100
result_2=100
print(result_1<=result_2)
print(result_1>=result_2)
print(result_1!=result_2)

# Logical operators

#and T T T
#or  T F T
#not F F F

name_1="raju"
name_2= 5.7
print(name_1 =="raju" and name_2 ==5.7)
print(name_1 =="rajesh" or name_2== 5.7)
sample=True
print(not(sample))
sample=False
print(not(sample))

#identity operators/ 2 variables check same memory location
# is/ python commanly cahes small intergers,trypically -5 to 256
#is not

a=12
print(id(a))
b=15
print(id(b))
print(a is b)
print(a is not b)

a=245
print(id(a))
b=245
print(id(b))
print(a is b)

#sequemce datatypes-->'str','list''tuple'
#order sequence of elements

adhar_name=["vasu","satya","lakshmi","raju","sai"]
print("raju" in adhar_name)
print("vinay"  not in adhar_name)


_name=["durga","devi"]
print("raju" in _name)
print("durga" in _name)
print(5 not in _name)

product_cost=10000
discount=10
result=product_cost*(discount/100)
#print(result)
product_cost-=result
#print(product_cost)
print(f"discount given{discount}%\nfinal discount{result}\ntotal cost after discount Rs{product_cost}/-")

#output (F-Strings)/consise and readible way
#easy insert variable into strings


 




















      













