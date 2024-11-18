import random
# Question 1
def remove_duplicates(nums:str) :
    num_list = []
    for i in nums:
        num_i = int(i)
        if num_i not in num_list:
            num_list.append(num_i)
    sorted_list = sorted(num_list)
    final_list = []
    for number in sorted_list:
        final_list.append(str(number))        
    return final_list


# given a string of numbers the function must return ,
# a list in ascending order without duplicates ,

# Question 2
def fun_triangle(height:int):
    # read the test for your clue .
    triangle = ""
    for i in range(1, height+1):
        rows = ""
        for j in range(1, i+1):
            rows += (str(i * j)) + " "
        triangle = rows
        print(triangle)        

     
def fun_triangle_upside_down(height:int):
    triangle = ""
    for i in range(1, height+1):
        count = height + 2
        rows = ""
        for j in range(1, count-i):
            rows += (str(j*i)) + " "
        triangle = rows
        print(triangle)


def im_a_hill_kinda(height:int):
    # hint: fusion ??or look at test ,look above.
    triangle = ""
    for i in range(1, height+1):
        rows = ""
        for j in range(1, i+1):
            rows += str(j*i) + " "
        triangle = rows
        print(triangle)
        
    for i in range(1, height+1):
        rows = ""
        count = height + 2
        for j in range(1, count-i):
            rows += str(j*i) + " "
        triangle = rows
        print(triangle)
    
# Question 3
def fizz_buzz(num:int):
    # google fizzbuzz lol or read the test but no chatgpt.
    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

# Question 4
def read_me():
    # open the lol.txt file
    # returns a list 
    f = open("lol.txt","r")
    
    return [word.strip() for word in f.readlines()] 

def validate_string(result:list):
    # I wish you all the best,read the test, also work as a team.
    # select a random word from the list
    # if the string has a length of four and contains more than one occurance of a letter return true else false
    if len(result) < 1:
        random_list = random.choice(result)
        chosen_word = random_list.lower()
    else:
        chosen_word = result.lower()
    word_list = []
    for cha in chosen_word.lower():
        word_list.append(cha.lower())
    if len(word_list) == 4:
        count = []
        for char in word_list:
            if char not in count:
                count.append(char)
        if len(count) != 2:
            return False
        else:
            return True
    else:
        return False

def simple_palidrome(word:str):
    # should the the word pass validation , check if it reads the same backwards , Anna is a palidrome
    # return the word is a palidrome.
    new_word = word[::-1]
    if new_word.lower() == word.lower():
        return f"{word} is a palidrome."
    else:
        return f"{word} is not a palidrome."

# Question 5
def give_me_the_digits(a_whole_list:list):
    # filter the list to only return the integers within mutiplied by 2
    #  [1,me,1,speed,5,7,9] should return [2,2,10,14,18]
    results = 0
    results_list = []
    
    for i in a_whole_list:
        try:
            results = int(i) * 2
            results_list.append(results)      
        except:
            continue
    return results_list
            
# Question 6 
def quick_maths(num1:str,num2:str,operation:str):
    # the point of this is problem solving , that said ,
    # this function must take the string and apply the operation
    # the parameter one ,one ,'+' should give me 2,
    # five * two must give me 10 , should the answer be greater than 10 return 'answer not supported'
    
    num_list = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,'nine':9, 'ten':10}
    for key, value in num_list.items():
        if key == num1.lower():
            number1 = value
        if key == num2.lower():
            number2 = value
            
    if operation == '/':
        total = number1 / number2
    elif operation == '*':
        total = number1 * number2
    elif operation == '+':
        total = number1 + number2
    elif operation == '-':
        total = number1 - number2
    if total > 10:
        return 'answer not supported'
    return total
      
# this is just for fun , dont't stress about it and keep it to your group .



