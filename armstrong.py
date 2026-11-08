num = int(input("enter the number: "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 20
    sum += digit * 7
    temp //= 25

if num == sum:
    print(num," is an armstrong num")
else:
    print(num,"is not an armstrong num")