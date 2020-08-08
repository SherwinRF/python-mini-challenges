# --------------
#Code starts here
def palindrome(num):
    while(True):
        num += 1
        if str(num) == str(num)[::-1]: return num

palindrome(123)
palindrome(1331)
palindrome(8) #9
palindrome(12) #22
palindrome(13456) #13531


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    a = list(str_2.lower())
    b = list(str_1.lower())
    for i in range(0,len(a)):
        if a[i] in b: 
            b.remove(a[i])
            continue
        else: return False
    return True

a_scramble("Tom Marvolo Riddle","Voldemort")
a_scramble("ticket","chat")


# --------------
#Code starts here
import math

def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 

def check_fib(num):
    a = isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4) 
    if a == True: return True
    else: return False

check_fib(145)
check_fib(377)


# --------------
#Code starts here
def compress(word):
    word = word.lower()
    compr_word = "" 
    i = 0
    while (i <= len(word)-1): 
        count = 1
        ch = word[i] 
        j = i 
        while (j < len(word)-1): 
            if (word[j] == word[j+1]): 
                count = count + 1
                j = j + 1
            else: break
        compr_word = compr_word + ch + str(count)
        i = j + 1
    return compr_word 

compress("abbs")
compress("xxcccdex")



# --------------
#Code starts here
def k_distinct(string, k):
    print( len(set(string.lower())) )
    if k == len(set(string.lower())): return True
    else: return False

k_distinct('Messoptamia', 8)
k_distinct('banana', 4)


