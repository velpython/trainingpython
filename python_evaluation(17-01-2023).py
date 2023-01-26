def Consonant(x):  
    print("--------Words formed by vel-----------")  
    a = print((user_input[0]), "2")
    b = print((user_input[1]), "1")
    c = print(user_input[:2] , "2")
    d = print(user_input[2:4], "1")
    e = print(user_input[0:3], "1")
    f = print(user_input[2:5], "1")
    g = print(user_input[0:4], "1")
    h = print(user_input[2:6], "1")
    k = print(user_input[:-1], "1")
    j = print(user_input , "1")

def vowels(x):
    print("-----words formed by ROss------")
    a1 = print((user_input[1]), "2")
    b1= print((user_input[3]), "1")
    c1 = print(user_input[1:3] , "2")
    d1 = print(user_input[3:5], "1")
    e1 = print(user_input[1:4], "1")
    f1 = print(user_input[1:5], "1")
    g1 = print(user_input[1:6], "1")

def vowels_consonant(string):
    n = len(string)
    comb = ((n)*(n+2))/4
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("The winner is : vel","\n","score:" ,  int(count_s) )
    else:
        print("The winner is : ROss", "\n","score : " , int(count_k))
if __name__ == '__main__':
    user_input = input("enter the word : ")
    Consonant(user_input)
    vowels(user_input)
    vowels_consonant(user_input)
