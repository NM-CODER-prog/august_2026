#LIST---COLLECTION if objects in orederd way.mutable

sample=[]
print(sample)
print(type(sample))


sample_2=[3,5,6,"pythonlife",(1,2,3),[1,2,3],{1,2,3},True,22,2,2,2,22,2,2]
print(sample_2)
print(type(sample_2))


#Indexing:ilist,tuple,string/indexing refers to the process of accessing individual elements.
#two type of indexing
#postive indexing(0 t0 n)
#negative indexing(-1 to n)

#list_1=[10,20,30,40,50,60,70,80]
#syntax
#seq[indexvalue]

list_1=[10,20,30,40,50,60,70,80]
print(list_1[3])
print(list_1[-5])
print(list_1[7])
print(list_1[-1])
print(list_1[0])
print(list_1[-8])


#slicing:slicing is away to extract a portion or a subsequence of elemensts
#syntax:
#seq(start:stop:step)
#forward direction-->postive index and negative index
#backword direction-->postive index and negative index


list_1=[10,20,30,40,50,60,70,80]
print(list_1[0:8:1])
print(list_1[::2])
print(list_1[::4])

list_1=[10,20,30,40,50,60,70,80]
print(list_1[5:])
print(list_1[:4:1])
print(list_1[-7:-4])
print(list_1[-8:-5])
print(list_1[-3::])

list_1=[10,20,30,40,50,60,70,80]
print(list_1[::-1])
print(list_1[6:3:-1])
print(list_1[2::-1])
print(list_1[3:1:-1])
print(list_1[-2:-5:-1])
print(list_1[3:1:-1])
print(list_1[-5:-7:-1])

matrix=[[1,2,4],[1,2,6],[1,2,3]]
print(matrix[1][2])
print(matrix[2][2])
print(matrix[0][2])
print(matrix[2][0])

#List Methods:
#append(),extend(),copy(),clear(),count(),inedx(),remove(),pop(),insert(),reverse() and sort().


#append-->add element:
#methodname(argument)#nothing but values.

numbers=[3,1,4,1,5,9,2,6,5]
print(numbers)
numbers.append([1,23,45,78,5,7])
print(numbers)


numbers=[3,1,4,1,5,9,2,6,5]
print(numbers)
numbers.extend(["pythonlife",1,23,45,78,5,7])#add list /multipul elements.
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5]#original data
sample=numbers.copy()
print(sample)
sample.append("pythonlife")#copy data
print(sample)
print(f"original data{numbers}")#not effected to original data.


numbers=[3,1,4,1,5,9,2,6,5]
numbers.clear()#give empty list
print(numbers)

number=[3,1,4,1,5,9,2,6,5]
print(number.count(9))#count list number
print(number.count("pythonlife"))

number=[3,1,4,1,5,9,2,6,5]
print(number.index(3))
print(number.index(4))
print(number.index(6))
print(number.index(5))#1st occurance

numbers=[3,1,4,1,5,9,2,6,5]
numbers.remove(3)#remove number
print(numbers)

numbers=[20,30,40,50]#index change after removing element
numbers.remove(40)
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5]
obj=numbers.pop(7)#heighlet one number/give index number
print(numbers)
print(obj)

numbers=[3,1,4,1,5,9,2,6,5]
numbers.insert(0,"pythonlife")# define index and element
print(numbers)
numbers.insert(20,"pythonlife")# define index out of range and element
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5]
numbers.reverse()
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5]
numbers.sort()#assending order
print(numbers)
numbers.sort(reverse=True)#disending oreder
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5]
print(len(numbers))

#List comprehensions:provide a concise way to craete list expression followed by for loop inside square brackets.
#syntax:
#[exp for item in iter]

for i in range(10):
    result=i**2
    print(type(result))

    empty_list=[]
    for i in range(10):
        result=i**2
        empty_list.append(result)
print(empty_list)

#[exp for iteam in seq]
result=[i**2 for i in range(10)]
print(result)
    
print([i**2 for i in range(10)])


for i in range(1,11):
    if(i%2==0):  
      print(i)

empty_list=[]
for i in range(1,11):
    if(i%2==0):
        empty_list.append(i)# show even numbers in list
print(empty_list)


#[exp for iteam in iter/seq if cond]#for faster exicution.
result = [i for i in range(1,11) if i%2==0]
print(result)

print([i for i in range(1,11) if i%2==0])

numbers=[3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1]#not valid 
sample=set(sample)
print(sample)

numbers=[3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1]
for i in numbers:
    if i == 1:
        numbers.remove(i)
print(numbers)

numbers=[3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1]
empty_list=[]
for i in numbers:
    if i!=1:
        empty_list.append(i)
print(empty_list)

numbers=[3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1]
print(len(numbers))
indexes=[]
for i in range(len(numbers)):
    if numbers[i]==1:
        indexes.append(i)
print(indexes)#return indexes in list

user_data=[]
for i in range(10):
    username=input("enter user name: ")
    user_data.append(username)
print(user_data)




























