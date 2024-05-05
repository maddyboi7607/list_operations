numbers=list(map(int,input().split()))
Max_numbers=max(numbers)
Min_numbers=min(numbers)
total_sum = sum(numbers)
count = len(numbers)
average = total_sum // count
print("1. Maximum number = ",Max_numbers)
print("2. Minimum number = ",Min_numbers)
print("3. Sum of the numbers = ",total_sum)
print("4. Average of the number = ", average)
a = []
b = []
for num in numbers:
    if num % 2 == 0:
        a.append(num)
    if num % 2 == 1:
        b.append(num)

list = set(numbers)
list.remove(max(list))
print("5. Second maximum number = ",max(list))
print("6. Even numbers = ",str(a).replace("[","").replace("]",""))
print("7. Odd numbers = ",str(b).replace("[","").replace("]",""))

c = []
for num in numbers:
    if 10 <= num <= 99:
        c.append(num)
print("8. Two digit numbers = ",str(c).replace("[","").replace("]",""))

neg = []
for num in numbers:
    if num<0:
        neg.append(num)
print("9. Negative numbers = ",str(neg).replace("[","").replace("]",""))

pos = []
for num in numbers:
    if num>0:
        pos.append(num)
print("10. Positive numbers = ",str(pos).replace("[","").replace("]",""))
