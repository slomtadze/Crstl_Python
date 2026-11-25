#1. შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად
#var1 = 1
#var2 = -1
#var3 = True
#print(var1, var2, var3)

var1 = int
var2 = int  
var3 = bool
print(var1, var2, var3)


#2. შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)
#var4 =False # გადაიყვანეთ Float -ში
#var5 =3 # გადაიყვანეთ Float -ში
#var6 = {"key":"value", "key1":"value", "key3":"value"} # გადაიყვანეთ list -ში
#print(var4, var5, var6)

var4 =False
var4 = float(var4)
var5 =3
var5 = float(var5)
var6 = {"key":"value", "key1":"value", "key3":"value"}
var6 = list(var6)
print(var4, var5, var6)



#3. შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის.
#group: #name: Python2023
#count: 35
#male: 22
#female: 13
#students: Student1, Student2, Student3, Student4, Student5
#ages: 24,33,15,45,42

name = "Python2023"
count = 35
male = 22
female = 13 
students = ["Student1", "Student2", "Student3", "Student4", "Student5"]
ages = [24,33,15,45,42]



#4. დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
#birth_year = 1970 # ჩაწერეთ წელი
#name = ‘სახელი’ #
#ჩაწერეთ სახელი
#surname = ‘გვარი’ # ჩაწერე გვარი
#current_year = ‘2025’
# უნდა მიიღოთ შემდეგი წინადადება - მე ‘სახელი’ ‘გვარი’ დავიბადე ‘ამ წელს’ შესაბამისად ვარ‘ამდენი წლის’

def calc_age(birth_year, current_year, name, surname):
    current_age = current_year - birth_year
    return f"მე {name} {surname} დავიბადე {birth_year} წელს შესაბამისად ვარ {current_age} წლის"
result = calc_age(1990, 2026, "საბა", "ლომთაძე")
print(result)

#5. გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.
#(შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე) მაგალითი: 
# YES: 1234=34.80%
# NO: 2312=65.20%
#Yes = 119
#No = 82
def calc_percentage(yes, no):
    total = yes + no
    yes_percentage = (yes / total) * 100
    no_percentage = (no / total) * 100
    return f"YES: {round(yes_percentage, 2)}% NO: {round(no_percentage, 2)}%"
calculation = calc_percentage(119, 82)  
print(calculation)

#6. გადაიყვანეთ 3670 წამი საათებად და წუთებად seconds = 3670 დაბეჭდეთ: "X საათი Y წუთი Z წამი"

seconds = 3670
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_left = ((seconds % 3600) % 60)
print(f"{hours} საათი {minutes} წუთი {seconds_left} წამი")

#7. გამოიტანეთ სტრიქონის პირველი და ბოლო ასო text = "Python"

text = "Python"
print(text[0], text[5])

#8. გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი math = 45 total = 60 დაბეჭდეთ: "პროცენტი: XX%"

math = 45
total = 60
print(f"პროცენტი: {math / total * 100} % ")

#9. გამოითვალეთ ასაკი მომავალ წელს #birth_year = 2000 #current_year = 2025 #დაბეჭდეთ ფორმატში:#“მომავალ წელს შენ იქნები XX წლის”

def count_age_next_year(birth_year, curr_year):
    age = curr_year - birth_year + 1
    print(age)

count_age_next_year(2000, 2025)
#10. 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ minutes = 350 მაგალითი: “X საათი და XX წუთი” 

print(f"{350 // 60} საათი და {350 % 60} წუთი")