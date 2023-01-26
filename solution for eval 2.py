import itertools

def check_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return c in vowels

def get_words_num(main_string, start_vowel):
    words_num = {}
    for i in range(len(main_string)):
        if (check_vowel(main_string[i]) and start_vowel) or (not check_vowel(main_string[i]) and not start_vowel):
            for j in range(i+1, len(main_string)+1):
                substring = main_string[i:j]
                if substring in words_num:
                    words_num[substring] += 1
                else:
                    words_num[substring] = 1
    return words_num

def scores_calc(main_string):
    ross_occurrence = get_words_num(main_string, False)
    print("Words formed by Ross: ")
    print(ross_occurrence)
    billy_occurrence = get_words_num(main_string, True)
    print("Words formed by Billy: ")
    print(billy_occurrence)
    ross_score = sum(ross_occurrence.values())
    billy_score = sum(billy_occurrence.values())
    if ross_score > billy_score:
        print("Ross wins with a score of", ross_score)
    elif billy_score > ross_score:
        print("Billy wins with a score of", billy_score)
    else:
        print("Draw")

if __name__ == "__main__":
     main_string = input("Enter the main string: ")
     scores_calc(main_string)