#добуток чисел заданого числа

number = 5896
mul = 1
while (number>0):
    rem = number%10
    mul = mul*rem
    number = number//10
print (mul)

#просортувати число

number = 5896
ascending = "".join(sorted(str(number)))
print (ascending)

#записати число в зворотньому порядку

num = 5896
number = str(num)
number = number[::-1]
print (number)
