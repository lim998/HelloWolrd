name='john smith'
numbers=[5,2,5,8,2]
tot=0
large=0


for i in ['mosy','mojang','jack']:
    print(i)

for i in range(5,10,2):#2 is step
    print(i)

for i in [10,20,30]:
    tot+=i

for i in numbers:
    output=""
    for z in range(i):
        output+="x"
    print(output)

numbers.append(14)
numbers.insert(0,23)
print(numbers)

print(numbers)
numbers.sort()
print(numbers)
numbers.pop() #remove last value
print(numbers)
numbers.reverse()
print(numbers)

for i in numbers:


    if i>large:
        large=i


print("large"+ str(large))

count=0
for i in numbers:
    count=numbers.count(i)
    if count>1:
        numbers.remove(i)

print(numbers)
