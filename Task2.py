from datetime import date
#1 გაქვთ ონლაინ მაღაზია, როდესაც მომხმარებელი შემოდის პროგრამის გაშვებისას უნდაგამოუჩნდეს მენიუ 
# მაგალითად: “გამარჯობა” თქვენ იმყოფებით მაღაზია SpaceX-ში, პროდუქტები:რაკეტა - 15000$, ხომალდი - 25000$, ჩაფხუტი - 5000$ და ა.შ. 
# მომხმარებელს უნდა ჰკითხოთრომელი ნივთები უნდა და დაუთვალოთ რა დაუჯდება ჯამურად, თუ დაგეთანხმებათ უნდა მიჰყიდოთნივთები
#  თუ უარს იტყვის შეთავაზებაზე უნდა დაასრულოთ მუშაობა.

products = {
    "რაკეტა" : 15000, 
    "ხომალდი" : 25000, 
    "ჩაფხუტი":5000
}

total_price = 0

print("გამარჯობა! თქვენ იმყოფებით მაღაზია SpaceX-ში.")
print("ჩვენი პროდუქტებია:")

for item, price in products.items():
    print(f"- {item}: {price}$")

while True:
    chosed_product = input("აირჩიეთ პროდუქტი ან მიუთითეთ 'დასრულება'")
    if chosed_product and chosed_product in products.keys():
        total_price += products[chosed_product]
        print(f"პროდუქტების ჯამური ფასია {total_price}$")
    elif chosed_product == "დასრულება":
        print("სესხია დასრულებულია")
        break
    else:
        print("არასწორი პროდუქტი, სცადეთ თავიდან")
        
#2 While loop და FOR LOOP-ის გამოყენებით დაწერეთ ციკლი, 
# რომელიც დაბეჭდავისას, გვერდითდაუწერს რიცხვს ლუწია თუ კენტი 20-მდე. (დაწერეთ ორივე ვარიანტი)
x=0
while x < 21:
    print(f"{x} - არის {"ლუწი" if x % 2 == 0 else "კენტი"}")
    x += 1

for x in range(21):
    print(f"{x} - არის {"ლუწი" if x % 2 == 0 else "კენტი"}")

#3 გამოითვალეთ თითოეული სტუდენტის საშუალო არითმეტიკული ქულა და დააბრუნეთ მისთვისშესაფერისი ნიშანი:
Students = {
    "Ana": [89,66,12,75,11],
    "Giorgi": [67,72,90,91,55],
    "Levani": [49,36,88,98,34],
    "Veronika": [99,88,32,65,99],
    "Nika": [77,81,41,73,99]
}
for student in Students.values():
    print(sum(student)/len(student))

#4 დაწერეთ ციკლი, რომელიც მოითხოვს მომხმარებლისგან ასაკის შეყვანას, თუ შეყვანილიმონაცემი არ იქნება რიცხვური ტიპის,
#  მაშინ ციკლი დატრიალდეს და თავიდან კითხოს, სხვაგვარადდაუანგარიშოს დაბადების თარიღი.
while True:
    age = input("შეიყვანეთ თქვენი ასაკი: ")
    if age.isdigit():
        print(f"{date.today().year - int(age)} - წელი")
        break
    else:
        print("შეიყვანეთ მხოლოდ ციფრები")


#5 While ციკლის მეშვეობით დაითვალეთ მოცემული მასივის: mylist = range(100) *მეორე ხარისხი *მესამე ხარისხი
mylist = range(100)
x = 2
while x < 4:
    for i in mylist:
        print(i ** x)
    x += 1

#6 FOR ციკლის/ციკლების გამოყენებით შექმენი გამრავლების ტაბულა და ტერმინალში გამოიტანემსგავსი ფორმატით:
for i in range(11):
    if i > 0:
        list = []
        for z in range (11):
            if z > 0:
                list.append(i*z)
        print(list)

#7 გააანალიზე კოდის ფრაგმენტი და შემდეგ გაასწორე შეცდომები, ასევე დაწერე ახსნა:
#numbers = ["1", "2", "3", "4"]
#total = 0
#for n in numbers:
    #total += n
    #print("Total:", total)

numbers = ["1", "2", "3", "4"]
total = 0
for n in numbers:
    total += int(n) #გადაყვანილია ინტ-ში სტრინგის ნაცვლად

print("Total:", total)

#8 გამოიყენე FOR ციკლი რომელიც მიწვდება data ყველა ელემენტს და დაწერე შემდეგი ლოგიკა, 
# თუელემენტი არის სტრინგი და შეიცავს მხოლოდ რიცხვს გადააქციე რიცხვად და შეინახე total-ში, 
# თურიცხვია პირდაპირ შეინახე total-ში, თუ სხვა ტიპის მონაცემთა ტიპია გამოტოვე. ბოლოს დაბეჭდესრული ჯამი.

data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for item in data:
    if type(item) == int:
        total += item
    elif type(item) == str and item.isdigit():
        total += int(item)
print("task 8 - ", total)

#9 დაწერეთ FOR LOOP სადაც მიწვდებით მონაცემებს, თუ მნიშვნელობა არის სტრინგი და შეიცავსმხოლოდ რიცხვს გამოიყენე კასტინგი და შეინახე, 
# თუ ინთეჯერია შეინახე პირდაპირ, თუ ბულიენიაგადააქციე და შეინახე (მხოლოდ True) სხვა ყველა ტიპის მონაცემი გამოტოვე.
transactions = {
"გიო": "100",
"ნიკა": 50,
"აკაკი": "30a",
"ლევანი": 0,
"ანა": "70",
"მარი": True
}
total = 0

for transaction in transactions.values():
    if type(transaction) == int:
        total += transaction
    elif type(transaction) == str and transaction.isdigit():
        total += int(transaction) 
    elif type(transaction) == bool and transaction:
        total += 1
    else:
        continue
print("Task 9 - ", total)

#10 შექმენი პროგრამა (თამაში) სადაც მომხმარებელი შეძლებს გამოიცნოს შენი ჩაწერილი რიცხვი,
# მომხმარებელი წერს ციფრებს და ცდილობს გამოიცნოს შენი რიცხვი, დიაპაზონი 0-დან 51-მდე, 
# თუმომხმარებელმა ჩაწერა ამ დიაპაზონს გარეთ უნდა გამოუტანო შეტყობინება რომ “რიცხვი სცდებაარეალს”, თუ ჩაწერა “exit” გამორთე თამაში, 
# უნდა დაუთვალო მცდელობების რაოდენობა დაგამოიტანო შეტყობინება: “გილოცავ გამოიცანი XX რიცხვი, მცდელობა: XX”
secret_number = 13
attemps = 0
print("თამაში დაიწყო")
while True:
    answer = input("შეყვანეთ თქვენი ციფრი: ")
    if answer.isdigit():
        if int(answer) < 0 or int(answer) > 51:
            print("რიცხვი სცდება არეალს")
        elif int(answer) == 13:
            attemps += 1
            print(f"გილოცავ გამოიცანი რიცხვი - {secret_number}, მცდელობა: {attemps}")
            break
        else:
            attemps += 1
            print("არასწორი პასუხი")
    elif answer == "exit":
        break
    else:
        print("გთხოვთ შეიყვანოთ მხოლოდ ციფრები")