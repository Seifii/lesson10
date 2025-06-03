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
    print("")
    cv2.imshow("Cat 2", image2)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 3", image3)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 4", image4)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 5", image5)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 6", image6)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 7", image7)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 8", image8)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 9", image9)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 10", image10)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 11", image11)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 12", image12)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 13", image13)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 14", image14)
    print("Другий і ************")
    n -= 1
    cv2.imshow("Cat 15", image15)
    print("Другий і ************")
    n -= 1

cv2.imshow("Hihiii", imagew)
cv2.waitKey()


