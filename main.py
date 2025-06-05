from csv import excel

import cv2

welcome = 'pass'
imagew = cv2.imread(welcome)

n = int()
rates = [14]

print(f"------------Котогалерея!------------")
cv2.imshow("Hihiii", imagew)
cv2.waitKey()

try:
    n = input(f"Введіть кількість котиків, яких ви хочете бачити сьогодні!(до 15): ")

except ValueError:
    print("Помилка. Перезапустіть програму")

else:
    print(f"Ok! сьогодні ви побачите {n} котиків і оціните їх від 1 до 10!")




cat1 = 'pass'
image1 = cv2.imread(cat1)
cat2 = 'pass'
image2 = cv2.imread(cat2)
cat3 = 'pass'
image3 = cv2.imread(cat3)
cat4 = 'pass'
image4 = cv2.imread(cat4)
cat5 = 'pass'
image5 = cv2.imread(cat5)
cat6 = 'pass'
image6 = cv2.imread(cat6)
cat7 = 'pass'
image7 = cv2.imread(cat7)
cat8 = 'pass'
image8 = cv2.imread(cat8)
cat9 = 'pass'
image9 = cv2.imread(cat9)
cat10 = 'pass'
image10 = cv2.imread(cat10)
cat11 = 'pass'
image11 = cv2.imread(cat11)
cat12 = 'pass'
image12 = cv2.imread(cat12)
cat13 = 'pass'
image13 = cv2.imread(cat13)
cat14 = 'pass'
image14 = cv2.imread(cat14)
cat15 = 'pass'
image15 = cv2.imread(cat15)
baraban = 'pass'
imageb = cv2.imread(baraban)

while n != 0:
    cv2.imshow("Cat 1", image1)
    print("Авввв! Він перший і ************")
    n -= 1
    rates[0] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 2", image2)
    print("Другий і ************")
    n -= 1
    rates[1] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 3", image3)
    print("Третій і ************")
    n -= 1
    rates[2] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 4", image4)
    print("Четвертий і ************")
    n -= 1
    rates[3] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 5", image5)
    print("П'ятий і ************")
    n -= 1
    rates[4] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 6", image6)
    print("Шостий і ************")
    n -= 1
    rates[5] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 7", image7)
    print("Сьомий і ************")
    n -= 1
    rates[6] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 8", image8)
    print("Восьмий і ************")
    n -= 1
    rates[7] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 9", image9)
    print("Дев'ятий і ************")
    n -= 1
    rates[8] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 10", image10)
    print("Десятий і ************")
    n -= 1
    rates[9] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 11", image11)
    print("Одинадцятий і ************")
    n -= 1
    rates[10] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 12", image12)
    print("Дванадцятий і ************")
    n -= 1
    rates[11] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 13", image13)
    print("Тринадцятий і ************")
    n -= 1
    rates[12] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 14", image14)
    print("Чотирнадцятий і ************")
    n -= 1
    rates[13] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 15", image15)
    print("Останній та п'ятнадцятий ************")
    n -= 1
    rates[15] = int(input("Оцініть котика від 1 до 10: "))

if max(rates) == rates[0]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 1", image1)
if max(rates) == rates[1]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 2", image2)
if max(rates) == rates[2]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 3", image3)
if max(rates) == rates[3]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 4", image4)
if max(rates) == rates[4]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 5", image5)
if max(rates) == rates[5]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 6", image6)
if max(rates) == rates[6]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 7", image7)
if max(rates) == rates[7]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 8", image8)
if max(rates) == rates[8]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 9", image9)
if max(rates) == rates[9]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 10", image10)
if max(rates) == rates[10]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 11", image11)
if max(rates) == rates[11]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 12", image12)
if max(rates) == rates[12]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 13", image13)
if max(rates) == rates[13]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 14", image14)
if max(rates) == rates[14]:
    print("Огооо! Найбільше вам сподобався ********")
    cv2.imshow("Cat 15", image15)



cv2.waitKey()


