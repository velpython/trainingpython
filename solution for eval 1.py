import re
def convert_expersion(expression):
    expression = correct_string.replace("[", "(").replace("]", ")")
    # convert the expression using raplace function with the brackets 
    expression1 = expression.replace("{", "(").replace("}", ")")
    if re.search("a-z", expression1):
        print("Error: The input contains non-numeric characters.")
    else:
        result_exp = eval(expression1)
        print("---------------------")
        print("Result : " , result_exp)
        # convert decimal to int 
        single_value = int(result_exp)
        while single_value  >= 10:
            single_value  = single_value  % 10 + single_value  // 10
    print("singular value :" , single_value)
    print("------------------------")
    return single_value

def is_prime(n): 
    i = 2
    if n <= 1:
        return False
    # for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        print(n, "is not a prime number")
        return False
    print(n , "is a prime")
    return True

def is_balanced(n):
    for i in range(n):
        if is_prime(i) and is_prime(n-i):
            print(n , "is not a balanced")
            # break   
            # return True
    print(n , "is a balanced")  
         
    # return False

if __name__ == "__main__":
    correct_string = "[[{15-7}*6]+[5678*2]-[7+(78/6)*{(8**2)+(56-45)}-(78%2)]+[(125+3785)]]"
    checking = convert_expersion(correct_string)
    print("...checking a number prime or balanced..")
    is_prime(checking)
    is_balanced(checking)