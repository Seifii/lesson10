from csv import excel

import cv2 #pip install opencv-python

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
    print("Авввв! Він перший і це Мейн-кун — одна з найбільших порід котів, вага може досягати 10 кг, а шерсть нагадує левову гриву.")
    n -= 1
    rates[0] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 2", image2)
    print("Другий - Сфінкс — лисий, але дуже теплий на дотик, бо його тіло виділяє більше тепла, ніж у звичайних котів.")
    n -= 1
    rates[1] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 3", image3)
    print("Третя Шотландська висловуха (Scottish Fold) — вуха загнуті вперед через генетичну мутацію, що також впливає на хрящі в тілі.")
    n -= 1
    rates[2] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 4", image4)
    print("Четвертий Бенгальський кіт — схожий на дикого леопарда, але має лагідну вдачу і дуже любить воду.")
    n -= 1
    rates[3] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 5", image5)
    print("П'ята Абіссінська кішка — схожа на мініатюрного пуму, розумна і грайлива.")
    n -= 1
    rates[4] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 6", image6)
    print("Шоста Персидська кішка — з розкішною шерстю і сплюснутим носом, відома своїм флегматичним темпераментом.")
    n -= 1
    rates[5] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 7", image7)
    print("Сьома - Орієнтальна кішка — має великі вуха, витончене тіло і голосний мяу, обожнює спілкування.")
    n -= 1
    rates[6] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 8", image8)
    print("Восьма Бірманська кішка — унікальне поєднання блакитних очей, білих лапок і шоколадного забарвлення.")
    n -= 1
    rates[7] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 9", image9)
    print("Дев'ятий Турецький ван — ще один кіт-любитель води, має цікаву особливість: зазвичай біле тіло і кольоровий хвіст.")
    n -= 1
    rates[8] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 10", image10)
    print("Десятий Рагдолл — назва перекладається як ганчіркова лялька, бо коти цієї породи буквально розслабляються на руках.")
    n -= 1
    rates[9] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 11", image11)
    print("Одинадцятий Сіамський кіт — має гучний голос і дуже емоційний характер, здатен розмовляти з власником")
    n -= 1
    rates[10] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 12", image12)
    print("Дванадцятий Корніш-рекс — має кучеряву шерсть, виглядає екзотично, схожий на інопланетянина.")
    n -= 1
    rates[11] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 13", image13)
    print("Тринадцята Норвезька лісова кішка — густе хутро захищає її від холоду, ідеально пристосована до скандинавського клімату.")
    n -= 1
    rates[12] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 14", image14)
    print("Чотирнадцятий Селкірк-рекс — кіт із кучерявою шерстю, ніби його завжди тільки-но причісували. Має спокійний, доброзичливий характер і виглядає дуже пухнастим, наче з мультфільму.")
    n -= 1
    rates[13] = int(input("Оцініть котика від 1 до 10: "))
    cv2.imshow("Cat 15", image15)
    print("Останній та п'ятнадцятий - ЛаПерм — ще один кучерявий красень, але з м’якішою шерстю, що утворює милі хвилі. Дуже товариський і допитливий, любить бути в центрі уваги.")
    n -= 1
    rates[14] = int(input("Оцініть котика від 1 до 10: "))

print("Тепер визначимось з результатами!")
cv2.imshow("Baraban", imageb)
print("Барабанний дрііііб.......")


if max(rates) == rates[0]:
    print("Огооо! Найбільше вам сподобався Мейн-кун")
    cv2.imshow("Cat 1", image1)
if max(rates) == rates[1]:
    print("Огооо! Найбільше вам сподобався Сфінкс")
    cv2.imshow("Cat 2", image2)
if max(rates) == rates[2]:
    print("Огооо! Найбільше вам сподобалась Шотландська висловуха")
    cv2.imshow("Cat 3", image3)
if max(rates) == rates[3]:
    print("Огооо! Найбільше вам сподобався Бенгальський кіт")
    cv2.imshow("Cat 4", image4)
if max(rates) == rates[4]:
    print("Огооо! Найбільше вам сподобалась Абіссінська кішка")
    cv2.imshow("Cat 5", image5)
if max(rates) == rates[5]:
    print("Огооо! Найбільше вам сподобалась Персидська кішка")
    cv2.imshow("Cat 6", image6)
if max(rates) == rates[6]:
    print("Огооо! Найбільше вам сподобалась Орієнтальна кішка")
    cv2.imshow("Cat 7", image7)
if max(rates) == rates[7]:
    print("Огооо! Найбільше вам сподобався Бірманська кішка")
    cv2.imshow("Cat 8", image8)
if max(rates) == rates[8]:
    print("Огооо! Найбільше вам сподобався Турецький ван")
    cv2.imshow("Cat 9", image9)
if max(rates) == rates[9]:
    print("Огооо! Найбільше вам сподобався Рагдолл")
    cv2.imshow("Cat 10", image10)
if max(rates) == rates[10]:
    print("Огооо! Найбільше вам сподобався Сіамський кіт")
    cv2.imshow("Cat 11", image11)
if max(rates) == rates[11]:
    print("Огооо! Найбільше вам сподобався Корніш-рекс")
    cv2.imshow("Cat 12", image12)
if max(rates) == rates[12]:
    print("Огооо! Найбільше вам сподобалась Норвезька лісова кішка")
    cv2.imshow("Cat 13", image13)
if max(rates) == rates[13]:
    print("Огооо! Найбільше вам сподобався Селкірк-рекс")
    cv2.imshow("Cat 14", image14)
if max(rates) == rates[14]:
    print("Огооо! Найбільше вам сподобався ЛаПерм")
    cv2.imshow("Cat 15", image15)



cv2.waitKey()


