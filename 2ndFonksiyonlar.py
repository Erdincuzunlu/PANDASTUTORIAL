#### LİSTE #####

print("a", "b")
print("c", "d", sep="--")


#### Fonksiyon tanımlama...

### girilen sayıları 2 ile çarpmak....

def calculate(x):
    print(x*2)


calculate(5)


### iki argümanlı parametreli bir fonksiyon tanımlayalım...


def summer(arg1, arg2):
    print(arg1 + arg2)

summer(5, 6)

summer(6, 5)
### sıralamanın da bir önemi olduğunu düşünüyorum burada...

#### Docstring

def summer(arg1, arg2):
    """

    Parameters
    sum of two numbers
    arg1 : int or float
    arg2 : int or float

    Returns int or float

    -------

    """
    print(arg1 + arg2)


#### def function_name(parameters/ arguments):
#statement ( function body)


def say_hi():
    print("Hello")
    print("How are you?")
    print("YOU are")


### girilen iki sayıyı çarpacak ve bunları bir argümanda tutacak bir fonksiyon yazalım..

def multiplication(arg1, arg2):
    c = arg1 * arg2
    print(c)





multiplication(5, 6)



#### girilen değerleri bir liste içinde saklayacak


list_store = []

def add(arg1, arg2):
    c = arg1 + arg2
    list_store.append(c)
    print(list_store)


add(5, 6)
add(2, 2)
add(180, 111)

list_store



### ön tanımlı argümanlar / parametreler ( default parameters / arguments)

def divide(arg1, arg2):
    print(arg1 / arg2)

divide(1, 2)



def divide(arg1, arg2=2):
    print(arg1 / arg2)

divide(10)


##### ne zaman fonksiyon yazma ihtiyacımız olur ?

### varm , moisture, charge

### DRY = dont repat urself...


def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(5, 5, 5)



#### return : fonksiyon çıktıklarını girdi olarak kullanmak....

def calculate(varm, moisture, charge):
    return(varm + moisture) / charge

calculate(5, 2, 5) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output

calculate(5, 2, 5)

varm, moisture, charge, output = calculate(5, 2, 5)


def standartization(a, p):
    return a * 10 / 100 * p * p

standartization(5, 2)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standartization(a, p)
    print(b * 10)

all_calculation(5, 2, 5, 2)


#### lokal ve global değişkenler kavramı...

list_store = [1, 2]

def add_elements(arg1, arg2):
    c = arg1 * arg2
    list_store.append(c)
    print(list_store)

add_elements(5, 2)


def new_elements(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

new_elements(5, 12)



def multiply_numbers(arg1, arg2):
    c = arg1 * arg2
    print(c)
multiply_numbers(5, 2)


def power(base, exponent=2):
    return base ** exponent

power(12, 3)
power(15,4)



def calculate_area(length, width):
    return length * width

calculate_area(5, 2)

# Fonksiyonu çağırın ve sonucu yazdırın

import math

def circle_circumference(radius):
    return 2 * math.pi * radius

circle_circumference(5)



#### for döngüsü

students = ["john", "mark", "venessa", "mariam"]

students[0]
students[1]
students[2]


for student in students:
    print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5999]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20/100 + salary))

def new_salary(salary, rate):
    return int(salary * rate/100 + salary)

new_salary(1500,20)
new_salary(1500,30)


for salary in salaries:
    print(new_salary(salary, 10))


for salary in salaries:
    if salary >= 2000:
        print(new_salary(salary, 20))
    else:
        print(new_salary(salary, 30))



### uygulama mülakat sorusu

### Amaç aşağıdaki şekilde string değiştiren bir fonksiyon yazacağız..


## Before : " hi my name is john and i am learning python"
## After : " Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

for i in range(len("miuul")):
    print(i)

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")


text = "hi my name is john and i am learning python"


modified_text = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])

print(modified_text)



salaries = [1000, 2000, 3000, 4000, 5999]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


salaries = [1000, 2000, 3000, 4000, 5999]
for salary in salaries:
    if salary >= 2000:
        continue
    print(salary)

names = ['Ali', 'Ayşe', 'Mehmet', 'Elif']

for index, name in enumerate(names):
    print(f"Index {index}: {name}")


students = ["john", "mark", "venessa", "mariam"]

A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
    print(index, student)

print("A listesi:", A)
print("B listesi:", B)


numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

even_index_numbers = []
odd_index_numbers = []

for index, number in enumerate(numbers):
    if number % 2 == 0:
        even_index_numbers.append(number)
    else:
        odd_index_numbers.append(number)

print(even_index_numbers)
print(odd_index_numbers)

students = ["john", "mark", "venessa", "mariam"]



def divide_students(students):
    group = [[], []]
    for index, student in enumerate(students):

        if index % 2 == 0:
            group[0].append(student)
        else:
            group[1].append(student)
    print(group)
    return group

st = divide_students(students)
st



def alternating_with_enumerate(string):
    new_string = ""
    for i,letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("hello darling how are you today")



names =  ["john", "mark", "venessa", "mariam"]
ages = [20, 13, 14, 21]

zipped = zip(names, ages)

for name, age in zipped:
    print(f"name: {name}, age: {age}")


    print(zipped)

#### LAmbda önemli kullan at fonksiyon döngü yazmadan sonuca varabiliriz.. map ise yazdığın fonksiyonlarda sana der ki
## bana bir fonksiyon ver o fonksiyonu nerede işleyeceğim bir argüman index vs ver ben onları birbiri ile eşliyim sonucu vereyim der.



salaries = [1000, 2000, 3000, 4000, 5999]

list(map(lambda x: x ** 2, salaries))

list(map(lambda x: x * 20 / 100 + x, salaries))




salaries = [1000, 2000, 3000, 3500, 3300, 3260, 3850, 3999, 4000, 4120, 4200, 5999]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))



salaries = [1000, 2000, 3000, 3500, 3300, 3260, 3850, 3999, 4000, 4120, 4200, 5999]


def new_salary(x):
    return x * 20 /100 + x

for salary in salaries:
    print(new_salary(salary))

bos_liste = []

for salary in salaries:
    bos_liste.append(new_salary(salary))

for salary in salaries:
    salary_rate = []
    if salary >3000:
        salary_rate.append(new_salary(salary))
    else:
        bos_liste.append(new_salary(salary))

print(bos_liste)
print(salary_rate)

salaries = [1000, 2000, 3000, 3500, 3300, 3260, 3850, 3999, 4000, 4120, 4200, 5999]

[salary * 2 for salary in salaries]


increased_salaries = [salary * 1.20 for salary in salaries if salary > 3000]
print(increased_salaries)
[salary * 2 for salary in salaries if salary > 3000]

[salary * 2 if salary > 3000 else salary * 3 for salary in salaries]


students = ["john", "mark", "venessa", "mariam"]

student_no = ["john", "Venessa"]




[student.lower() if student in student_no else student.upper() for student in students]



dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4,}

dictionary.keys()
dictionary.values()
dictionary.items()


{k: v ** 2 for (k, v) in dictionary.items()}


{k.upper(): v  for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}


##### amaç çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir....
### key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak...


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}



##### bir veri stetindeki değişken isimlerini değiştirmek.


["total", "spending", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses", "abbrev"]



import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns