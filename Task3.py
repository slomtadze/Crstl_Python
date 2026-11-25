import random

#1 დაწერეთ პირობა, რომელიც გაარკვევს შემოტანილი ასო არის თანხმოვანი თუ ხმოვანი მაგალითი:
# შემოიტანე სიმბოლო: ბ "ბ" თანხმოვანია 
# ===================== 
# შემოიტანე სიმბოლო: ი "ი" ხმოვანია 
# =====================

# vovel = "აეიოუ"
# while True:
#     letter = input("შემოიტანე სიმბოლო ან მიუთითეთ 'დასრულება': ")
#     letter = letter.strip()
#     if letter == "დასრულება":
#         print("სესია დასრულებულია \n ===================== ")
#         break
#     elif len(letter) != 1:
#         print("შეიყვანეთ მხოლოდ ერთი სიმბოლო \n =====================")
#     elif letter.isalpha():
#         print(f"{letter} {"ხმოვანია" if letter in vovel else "თანხმოვანია"} \n =====================")
#     else:
#         print("შეიყვანეთ მხოლოდ ასო \n =====================")


#2 დაწერე პირობა რომელიც for ციკლის გამოყენებით გამოიტანს რიცხვებს 10-დან 0-მდე

# for i in range(10, 0, -1):
#     print(i) #0-იანის დაწერაც თუ გვინდა 0-ს ნაცვლად იქნება -1


#3 დაწერეთ ციკლი რომელიც დაბეჭდავს ლისტში მყოფ უდიდეს 3 რიცხვს და მათ ინდექსებს

# lst = [random.randint(1,20) for _ in range(10)] # ქმნის და ინახავს random მონაცემებს [1,4,2,3,6,5]
# print(lst)

# მაგალითი:
# [3, 14, 4, 1, 2, 11, 12, 18, 7, 18]
# მონაცემი 1: 18
# მონაცემი 2: 18
# მონაცემი 3: 14

# lst = [random.randint(1,20) for _ in range(10)]
# lst_sort = []

# for num in lst:
#     lst_sort.append(num)
# lst_sort.sort(reverse=True)

# for index, num in enumerate(lst_sort):
#     if index < 3:
#         original_index = lst.index(num)
#         print(f"მონაცემი {index + 1}: {num} - ინდექსი [{original_index}]")
#     else:
#         break

#4 დაწერეთ ციკლი რომელიც დაბეჭდავს ოთხუთხედს “#” (ასეთს) მოცემული სიმაღლისა და სიგანის მიხედვით

#       მაგალითი:
#       width=5
#       height=2
#       # # # # #
#       # # # # #

# height=random.randrange(1,10)
# width=random.randrange(1,10)

# for lines in range(height):
#     symbol = "#"
#     print(" ".join([symbol] * width))

#5 მომხმარებელს შემოყავს ორი რიცხვი x & y შექმენით ფუნქცია, 
#  რომელიც მიიღებს ამ ორ პარამეტრს და დაბეჭდავს ყველა არითმეტიკულ ოპერაციას

# def calc(x,y):
#     sum = x + y
#     sub = x - y
#     mult = x * y
#     div = x / y
#     floor_div = x // y
#     mod = x % y
#     return (sum ,sub, mult, div, floor_div, mod)

# result = calc(random.randrange(1,10),random.randrange(1,10))
# print(result)

#6 გადააქციეთ დავალება #4 ფუნქციად,
# რომელსაც ექნება 2 პარამეტრი სიმაღლე, სიგანე

# def draw_symbols(height, width):
#     symbol_line = ' '.join(["#"] * width)
#     str = "\n".join([symbol_line] * height)
#     return str

# output = draw_symbols(random.randrange(1,10),random.randrange(1,10))
# print(output)

#7 დაწერეთ ფუნქცია, რომელიც მიიღებს 2 პარამეტრს:
#  სტრიქონს და სიმბოლოს ფუნქციამ უნდა დაითვალოს თუ რამდენჯერ გვხვდება სიმბოლო სტიქონში.

# def count_symbol(str, symb):    
#     count = str.lower().count(symb.lower())
#     return count

# output = count_symbol("John and Jane Doe", "d")
# print(f"Character in given string: {output} times")

#8 დაწერეთ ფუნქცია რომელიც დაითვლის სიტყვების რაოდენობას წინადადებაში.

# def calc_words(str):
#     str_lst = str.split()
#     return len(str_lst)

# output = calc_words("რამდენიმე სიტყვა, რომლის დათვლასაც ვაპირებთ")
# print(output)

#9 შექმენი თამაში hangman სიტყვის გამოცნობა… კომპიუტერი ირჩევს “შემთხვევით” სიტყვას და მომხმარებელს აქვს 10 ცდა სიტყვის გამოსაცნობად, 
# მომხმარებელს აქვს ასოების ჩაწერის უფლება და ასევე სიტყვის ჩაწერის უფლება სრულად, 
# თუ სიტყვას 10 ცდაში გამოიცნობს გამოიტანოს “გილოცავ” თუ ვერ გამოიტანოს “თქვენ დამარცხდით” თამაშის გამორთვა “exit”\

# count = 10
# word_lst = ["apple", "crane", "slate", "ghost", "planet", "bridge", "castle", "python", "rhythm", "zephyr", "sphinx", "oxygen"]
# secret_word = random.choice(word_lst)
# hidden_secret_word = "#" * len(secret_word)
# #print(secret_word)

# while True:    
#     if count < 1:
#         print("თქვენ დამარცხდით")
#         break
#     user_answ = input("შეიყვანეთ ასო ან სიტყვა:  \n თამაშის გასათიშად მიუთითეთ 'exit' ")
#     if user_answ == "exit":
#         print("თამაში დასრულებულია \n =====================")
#         break
#     elif not user_answ.isalpha():
#         print("შეიყვანეთ მხოლოდ ასოები \n =====================")
#         continue
#     elif len(user_answ) > 1:
#         if user_answ.lower() == secret_word:
#             print("გილოცავ, თქვენ გამოიცანით სიტყვა \n =====================")
#             print("თამაში დასრულებულია")
#             break
#         else:
#             print("არასწორი სიტყვა \n =====================")
#             count -= 1
#             continue
#     elif len(user_answ) == 1:
#         letter_is_in_word = secret_word.find(user_answ.lower())
#         if letter_is_in_word == -1:
#             print("ასო არ მოიძებნა \n =====================") 
#             count -= 1
#         else: 
#            count -= 1           
#            for index, letter in enumerate(secret_word):
#                if letter == user_answ.lower():
#                    hidden_secret_word_lst = list(hidden_secret_word)
#                    hidden_secret_word_lst[index] = letter
#                    hidden_secret_word = "".join(hidden_secret_word_lst)  
#         letters_remaining = hidden_secret_word.find("#")
#         if letters_remaining == -1:
#             print("გილოცავ, თქვენ გამოიცანით სიტყვა \n =====================")
#             print("თამაში დასრულებულია")
#             break
#         else:
#             print(hidden_secret_word, "დარჩენილი ცდა", count)


#10 შექმენი პატარა თამაში სადაც მომხმარებელს აქვს ორი არჩევანი “მარჯვენა” ან “მარცხენა” 
# პროგრამამ შემთხვევითობის პრინციპით უნდა გაანაწილოს რომელია სწორი “მარჯვენა” თუ “მარცხენა”, 
# თუ მომხმარებელი 5 ცდიდან ყველა სწორ მიმართულებას აირჩევს გამოიტანე “გამარჯვება” სხვა შემთხვევაში “შენ დამარცხდი”, თამაშის გამორთვა “exit”
    
# count = 0
# while True:
#     right_choise = f"{"მარჯვენა" if random.randint(0,1) == 1 else "მარცხენა"}"  
#     user_answ = input("შეიყვანეთ მიმართულება, მხოლოდ სიტყვა 'მარჯვენა' ან 'მარცხენა'. \n თამაშის გამოსართავად მიუთითე 'exit': ")
#     if user_answ.strip() == "exit":
#         print("თამაში დასრულებულია \n")
#         break 
#     if user_answ == "მარჯვენა" or user_answ == "მარცხენა":
#         if user_answ.strip() != right_choise:
#             print("შენ დამარცხდი, თამაში დასრულებულია \n")
#             break
#         elif count == 4:
#             print("გამარჯვება \n")
#             break
#         else:
#             print("სწორი პასუხი \n")
#             count +=1              
#     else:
#         print("შეიყვანეთ მხოლოდ მითითებული სიტყვები \n")  
        
        



         
            


