#tranferstatement:
#break--exit the loop prematurly/immediatly terminate the loop
#syntax:
#for iteam in iterable:
    #if condition:
        #break

#for i in range(10):
    #print(f"{i}")

for i in range(10):
    if i==3:
        break
    print(i)
print(f"last iteration{i}")

students=["vasu","kiran","soni","pavan","raghu","ram"]
for i in students:
    print(i)
print(f"last iteration {i}")#last itaration print


students=["vasu","kiran","soni","pavan","raghu","ram"]
for i in students:
    if i=="pavan":
        print(f"student found{i}")
        break
print(f"last iteration {i}")#last ittaration pavan


company_name="ABC"
company_employes=[123,134,456,789,456,567,890,345,678,234,567,891]
for i in company_employes:
    if i==345:
        print(f"id fount{i}")
        break#break the loop /dont go to next ittaration
print(f"last itaratio{i}")

#continue:statement is used to skip /
#syntax:
"""for iteam in iterable:
    if condition:
        continue
    code here will be skipped if the condition is met"""

for i in range(10):
    if i == 3:
        continue#condition is true skip the 3 and contine with next itaration.
    print(f"{i}")

for i in range(1,100):
    if i==71:
        continue
    print(f"{i}")

products=["ok","ok","defect","defect","ok","ok","ok","defect"]
for i in products:
    if i=="defect":
       continue
    print(f"{i}")

#pass-- pass statement null operation/its act like placeholder/code is required but yet decited

for i in range(10):#itaration done 
    pass#hold the place for code
print(i)

age=35
if age>=35:
    pass
print(age)#last itaration

#LIST---COLLECTION if objects in orederd way.mutable




  





