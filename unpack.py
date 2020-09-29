#dictionary
customer= {
    "name":"Lim",
    "age":"14"
}

numbers={
    "1":"one",
    "2":"two",
    "3":"three"
}
inp=input("")
num=""
for i in inp:

    num=num+" "+numbers[i]
print(num)
print(customer["name"])
print(customer.get("name"))
print(customer.get("sex","male"))  #add default value
customer["sex"]="female"
print(customer["sex"])
number=(1,2,3)
num=number[0]
num2=number[1]
num3=number[2]

print (num,num2,num3)

x,y,z=number
print(x,y,z)