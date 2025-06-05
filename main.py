from csv import excel
from PIL import Image #pip install pillow

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
cat_face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image1 = cv2.imread(cat1)
cat_face1 = cat_face_cascade1.detectMultiScale(image1)
cat1 = Image.open(image1)

cat1 = cat1.convert("RGBA")

cat2 = 'pass'
cat_face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image2 = cv2.imread(cat2)
cat_face2 = cat_face_cascade2.detectMultiScale(image2)
cat2 = Image.open(image2)

cat2 = cat2.convert("RGBA")

cat3 = 'pass'
cat_face_cascade3 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image3 = cv2.imread(cat3)
cat_face3 = cat_face_cascade3.detectMultiScale(image3)
cat3 = Image.open(image3)

cat3 = cat3.convert("RGBA")

cat4 = 'pass'
cat_face_cascade4 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image4 = cv2.imread(cat4)
cat_face4 = cat_face_cascade4.detectMultiScale(image4)
cat4 = Image.open(image3)

cat4 = cat4.convert("RGBA")

cat5 = 'pass'
cat_face_cascade5 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image5 = cv2.imread(cat5)
cat_face5 = cat_face_cascade5.detectMultiScale(image5)
cat5 = Image.open(image5)

cat5 = cat5.convert("RGBA")
cat6 = 'pass'
cat_face_cascade6 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image6 = cv2.imread(cat6)
cat_face6 = cat_face_cascade6.detectMultiScale(image6)
cat6 = Image.open(image6)

cat6 = cat6.convert("RGBA")

cat7 = 'pass'
cat_face_cascade7 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image7 = cv2.imread(cat7)
cat_face7 = cat_face_cascade7.detectMultiScale(image7)
cat7 = Image.open(image7)

cat7 = cat7.convert("RGBA")

cat8 = 'pass'
cat_face_cascade8 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image8 = cv2.imread(cat8)
cat_face8 = cat_face_cascade8.detectMultiScale(image8)
cat8 = Image.open(image8)

cat8 = cat8.convert("RGBA")

cat9 = 'pass'
cat_face_cascade9 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image9 = cv2.imread(cat9)
cat_face9 = cat_face_cascade9.detectMultiScale(image9)
cat9 = Image.open(image9)

cat9 = cat9.convert("RGBA")

cat10 = 'pass'
cat_face_cascade10 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image10 = cv2.imread(cat10)
cat_face10 = cat_face_cascade2.detectMultiScale(image10)
cat10 = Image.open(image10)

cat10 = cat10.convert("RGBA")

cat11 = 'pass'
cat_face_cascade11 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image11 = cv2.imread(cat11)
cat_face11 = cat_face_cascade11.detectMultiScale(image11)
cat11 = Image.open(image11)

cat11 = cat11.convert("RGBA")

cat12 = 'pass'
cat_face_cascade12 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image12 = cv2.imread(cat12)
cat_face12 = cat_face_cascade12.detectMultiScale(image12)
cat12 = Image.open(image12)

cat12 = cat12.convert("RGBA")

cat13 = 'pass'
cat_face_cascade13 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image13 = cv2.imread(cat13)
cat_face13 = cat_face_cascade1.detectMultiScale(image13)
cat13 = Image.open(image13)

cat13 = cat13.convert("RGBA")

cat14 = 'pass'
cat_face_cascade14 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image14 = cv2.imread(cat14)
cat_face14 = cat_face_cascade14.detectMultiScale(image14)
cat14 = Image.open(image14)

cat14 = cat14.convert("RGBA")

cat15 = 'pass'
cat_face_cascade15 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image15 = cv2.imread(cat15)
cat_face15 = cat_face_cascade15.detectMultiScale(image15)
cat15 = Image.open(image15)

cat15 = cat15.convert("RGBA")

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


