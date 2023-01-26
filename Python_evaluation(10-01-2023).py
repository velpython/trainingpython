import re
import math

#  Q1 check syntax 
correct_string = "[[{15-7}*6]+[5678*2]-[7+(78/6)*{(8**2)+(56-45)}-(78%2)]+[(125+3785)]]"
brackets_check = ["[{15-7}*6]+[5678*2]-[7+(78/6)*{(8**2)+(56-45)}-(78%2)]+(125+3785)"]

def check(my_string):
    global brackets_check
    while any(x in my_string for x in brackets_check):
        for br in brackets_check:
            my_string = my_string.replace(br, '')
    return not my_string
print(""
      if check(correct_string) else "The given expression is wrong --- " +  "\ncorrect syntax is :" + correct_string)

# Q2 checking alphabets 

number_or_symbol = re.compile('\s*([()]|\d+)')
number_or_symbol1 = (re.findall(number_or_symbol, correct_string))
a_list = []
for alphabets in number_or_symbol1:
    print(alphabets)
    check_alphablet = any(alphabets.isalpha()for char in alphabets)
   
    a_list.append(alphabets)
    
    # print(re.findall(number_or_symbol1, correct_string))
    if check_alphablet == False :
        None
    else:
        print("its contain alphabets")
print(a_list)

# Q4 calculation 

a , b , c  =  int(a_list[0]) , int(a_list[1]) , int(a_list[2]) 
d , e , f =  int(a_list[3]) , int(a_list[4]) , int(a_list[5]) 
g , h , i = int(a_list[7]) , int(a_list[8]) , int(a_list[11])
# # j , k , l   = int(a_list[14]) , int(a_list[15]) , int(a_list[18])
# m , n , o = int(a_list[19]),int(a_list[22]),int(a_list[23])
checked_value = ((a - b*c) + (d*e) - (f + (g / h)))

 # Q5 


num_checking_prime = checked_value
# for i in num_checking_prime:
#     if 1 <= x <= 9:
#         print(x)
#         break
#     else:
#         one = x % 10
#         two = math.floor(x / 10)
#         print(one,two)
#         x = one + two
# n = 11309
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += float(digit)
#         print(digit)
#     return sum
# print("total sum", (getSum(n)))
if num_checking_prime > 1:
    for i in range(2, int(num_checking_prime/2)+1):
        if (num_checking_prime % i) == 0:
            print(num_checking_prime, "is not a prime number")
            break
    else:
        print(num_checking_prime, "is a prime number")
else:
    print(num_checking_prime, "is not a prime number")


