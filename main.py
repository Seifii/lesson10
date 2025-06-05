from csv import excel
from PIL import Image #pip install pillow

import cv2 #pip install opencv-python


welcome = 'welcome.jpg'
imagew = cv2.imread(welcome)

# n = int()
rates = [0] * 15

print(f"------------Котогалерея!------------")
cv2.imshow("Hihiii", imagew)
cv2.waitKey()
print("Вітаю! Сьогодні ви побачите 15 котиків, дізнаєтесь про них щось нове та оціните їх від 1 до 10!")
# try:
#     n = int(input(f"Введіть кількість котиків, яких ви хочете бачити сьогодні!(до 15): "))
#
# except ValueError:
#     print("Помилка. Перезапустіть програму")
#
# else:
#     print(f"Ok! сьогодні ви побачите {n} котиків і оціните їх від 1 до 10!")
#
#


cat1s = 'Cat1.png'
cat_face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image1 = cv2.imread(cat1s)
cat_face1 = cat_face_cascade1.detectMultiScale(image1)
cat1 = Image.open(cat1s)

cat1 = cat1.convert("RGBA")

cat2s = 'Cat2.jpg'
cat_face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image2 = cv2.imread(cat2s)
cat_face2 = cat_face_cascade2.detectMultiScale(image2)
cat2 = Image.open(cat2s)

cat2 = cat2.convert("RGBA")

cat3s = 'Cat3.jpg'
cat_face_cascade3 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image3 = cv2.imread(cat3s)
cat_face3 = cat_face_cascade3.detectMultiScale(image3)
cat3 = Image.open(cat3s)

cat3 = cat3.convert("RGBA")

cat4s = 'Cat4.jpg'
cat_face_cascade4 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image4 = cv2.imread(cat4s)
cat_face4 = cat_face_cascade4.detectMultiScale(image4)
cat4 = Image.open(cat4s)

cat4 = cat4.convert("RGBA")

cat5s = 'Cat5.jpg'
cat_face_cascade5 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image5 = cv2.imread(cat5s)
cat_face5 = cat_face_cascade5.detectMultiScale(image5)
cat5 = Image.open(cat5s)

cat5 = cat5.convert("RGBA")
cat6s = 'Cat6.jpg'
cat_face_cascade6 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image6 = cv2.imread(cat6s)
cat_face6 = cat_face_cascade6.detectMultiScale(image6)
cat6 = Image.open(cat6s)

cat6 = cat6.convert("RGBA")

cat7s = 'Cat7.jpg'
cat_face_cascade7 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image7 = cv2.imread(cat7s)
cat_face7 = cat_face_cascade7.detectMultiScale(image7)
cat7 = Image.open(cat7s)

cat7 = cat7.convert("RGBA")

cat8s = 'Cat8.jpg'
cat_face_cascade8 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image8 = cv2.imread(cat8s)
cat_face8 = cat_face_cascade8.detectMultiScale(image8)
cat8 = Image.open(cat8s)

cat8 = cat8.convert("RGBA")

cat9s = 'Cat9.jpg'
cat_face_cascade9 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image9 = cv2.imread(cat9s)
cat_face9 = cat_face_cascade9.detectMultiScale(image9)
cat9 = Image.open(cat9s)

cat9 = cat9.convert("RGBA")

cat10s = 'Cat10.jpg'
cat_face_cascade10 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image10 = cv2.imread(cat10s)
cat_face10 = cat_face_cascade2.detectMultiScale(image10)
cat10 = Image.open(cat10s)

cat10 = cat10.convert("RGBA")

cat11s = 'Cat11.jpg'
cat_face_cascade11 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image11 = cv2.imread(cat11s)
cat_face11 = cat_face_cascade11.detectMultiScale(image11)
cat11 = Image.open(cat11s)

cat11 = cat11.convert("RGBA")

cat12s = 'Cat12.jpg'
cat_face_cascade12 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image12 = cv2.imread(cat12s)
cat_face12 = cat_face_cascade12.detectMultiScale(image12)
cat12 = Image.open(cat12s)

cat12 = cat12.convert("RGBA")

cat13s = 'Cat13.jpg'
cat_face_cascade13 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image13 = cv2.imread(cat13s)
cat_face13 = cat_face_cascade1.detectMultiScale(image13)
cat13 = Image.open(cat13s)

cat13 = cat13.convert("RGBA")

cat14s = 'Cat14.jpg'
cat_face_cascade14 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image14 = cv2.imread(cat14s)
cat_face14 = cat_face_cascade14.detectMultiScale(image14)
cat14 = Image.open(cat14s)

cat14 = cat14.convert("RGBA")

cat15s = 'Cat15.jpg'
cat_face_cascade15 = cv2.CascadeClassifier('haarcascade_frontalcatface_extended (2).xml')
image15 = cv2.imread(cat15s)
cat_face15 = cat_face_cascade15.detectMultiScale(image15)
cat15 = Image.open(cat15s)

cat15 = cat15.convert("RGBA")

mask = Image.open('mask.png')
mask = mask.convert("RGBA")

baraban = 'baraban.png'
imageb = cv2.imread(baraban)

# while n != 0:
cv2.imshow("Cat 1", image1)
cv2.waitKey()
print("Авввв! Він перший і це Мейн-кун — одна з найбільших порід котів, вага може досягати 10 кг, а шерсть нагадує левову гриву.")
#n = n - 1
rates[0] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face1:
    mask = mask.resize((w+15, h+15))
    cat1.paste(mask, (x, y), mask)
    cat1.save("cat_star1.png")
    cat_star1 = cv2.imread("cat_star1.png")
    cv2.imshow("Cat_star1", cat_star1)
    cv2.waitKey()
cv2.imshow("Cat 2", image2)
cv2.waitKey()
print("Другий - Сфінкс — лисий, але дуже теплий на дотик, бо його тіло виділяє більше тепла, ніж у звичайних котів.")
#n = n - 1
rates[1] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face2:
    mask = mask.resize((w, h))
    cat2.paste(mask, (x, y), mask)
    cat2.save("cat_star2.png")
    cat_star2 = cv2.imread("cat_star2.png")
    cv2.imshow("Cat_star2", cat_star2)
    cv2.waitKey()

cv2.imshow("Cat 3", image3)
cv2.waitKey()
print("Третя Шотландська висловуха (Scottish Fold) — вуха загнуті вперед через генетичну мутацію, що також впливає на хрящі в тілі.")
#n = n - 1
rates[2] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face3:
    mask = mask.resize((w, h))
    cat3.paste(mask, (x, y), mask)
    cat3.save("cat_star3.png")
    cat_star3 = cv2.imread("cat_star3.png")
    cv2.imshow("Cat_star3", cat_star3)
    cv2.waitKey()

cv2.imshow("Cat 4", image4)
cv2.waitKey()
print("Четвертий Бенгальський кіт — схожий на дикого леопарда, але має лагідну вдачу і дуже любить воду.")
#n = n - 1
rates[3] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face4:
    mask = mask.resize((w, h))
    cat4.paste(mask, (x, y), mask)
    cat4.save("cat_star4.png")
    cat_star4 = cv2.imread("cat_star4.png")
    cv2.imshow("Cat_star4", cat_star4)
    cv2.waitKey()

cv2.imshow("Cat 5", image5)
cv2.waitKey()
print("П'ята Абіссінська кішка — схожа на мініатюрного пуму, розумна і грайлива.")
#n = n - 1
rates[4] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face5:
    mask = mask.resize((w, h))
    cat5.paste(mask, (x, y), mask)
    cat5.save("cat_star5.png")
    cat_star5 = cv2.imread("cat_star5.png")
    cv2.imshow("Cat_star5", cat_star5)
    cv2.waitKey()

cv2.imshow("Cat 6", image6)
cv2.waitKey()
print("Шоста Персидська кішка — з розкішною шерстю і сплюснутим носом, відома своїм флегматичним темпераментом.")
#n = n - 1
rates[5] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face6:
    mask = mask.resize((w, h))
    cat6.paste(mask, (x, y), mask)
    cat6.save("cat_star6.png")
    cat_star6 = cv2.imread("cat_star6.png")
    cv2.imshow("Cat_star6", cat_star6)
    cv2.waitKey()

cv2.imshow("Cat 7", image7)
cv2.waitKey()
print("Сьома - Орієнтальна кішка — має великі вуха, витончене тіло і голосний мяу, обожнює спілкування.")
#n = n - 1
rates[6] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face7:
    mask = mask.resize((w, h))
    cat7.paste(mask, (x, y), mask)
    cat7.save("cat_star7.png")
    cat_star7 = cv2.imread("cat_star7.png")
    cv2.imshow("Cat_star7", cat_star7)
    cv2.waitKey()

cv2.imshow("Cat 8", image8)
cv2.waitKey()
print("Восьма Бірманська кішка — унікальне поєднання блакитних очей, білих лапок і шоколадного забарвлення.")
#n = n - 1
rates[7] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face8:
    mask = mask.resize((w, h))
    cat8.paste(mask, (x,y), mask)
    cat8.save("cat_star8.png")
    cat_star8 = cv2.imread("cat_star8.png")
    cv2.imshow("Cat_star8", cat_star8)
    cv2.waitKey()

cv2.imshow("Cat 9", image9)
cv2.waitKey()
print("Дев'ятий Турецький ван — ще один кіт-любитель води, має цікаву особливість: зазвичай біле тіло і кольоровий хвіст.")
#n = n - 1
rates[8] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face9:
    mask = mask.resize((w, h))
    cat9.paste(mask, (x, y), mask)
    cat9.save("cat_star9.png")
    cat_star9 = cv2.imread("cat_star9.png")
    cv2.imshow("Cat_star9", cat_star9)
    cv2.waitKey()

cv2.imshow("Cat 10", image10)
cv2.waitKey()
print("Десятий Рагдолл — назва перекладається як ганчіркова лялька, бо коти цієї породи буквально розслабляються на руках.")
#n = n - 1
rates[9] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face10:
    mask = mask.resize((w, h))
    cat10.paste(mask, (x, y), mask)
    cat10.save("cat_star10.png")
    cat_star10 = cv2.imread("cat_star10.png")
    cv2.imshow("Cat_star10", cat_star10)
    cv2.waitKey()

cv2.imshow("Cat 11", image11)
cv2.waitKey()
print("Одинадцятий Сіамський кіт — має гучний голос і дуже емоційний характер, здатен розмовляти з власником")
#n = n - 1
rates[10] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face11:
    mask = mask.resize((w, h))
    cat11.paste(mask, (x, y), mask)
    cat11.save("cat_star11.png")
    cat_star11 = cv2.imread("cat_star11.png")
    cv2.imshow("Cat_star11", cat_star11)
    cv2.waitKey()

cv2.imshow("Cat 12", image12)
cv2.waitKey()
print("Дванадцятий Корніш-рекс — має кучеряву шерсть, виглядає екзотично, схожий на інопланетянина.")
#n = n - 1
rates[11] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face12:
    mask = mask.resize((w, h))
    cat12.paste(mask, (x, y), mask)
    cat12.save("cat_star12.png")
    cat_star12 = cv2.imread("cat_star12.png")
    cv2.imshow("Cat_star1", cat_star12)
    cv2.waitKey()

cv2.imshow("Cat 13", image13)
cv2.waitKey()
print("Тринадцята Норвезька лісова кішка — густе хутро захищає її від холоду, ідеально пристосована до скандинавського клімату.")
#n = n - 1
rates[12] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face13:
    mask = mask.resize((w, h))
    cat13.paste(mask, (x, int(y + h / 3)), mask)
    cat13.save("cat_star13.png")
    cat_star13 = cv2.imread("cat_star13.png")
    cv2.imshow("Cat_star13", cat_star13)
    cv2.waitKey()

cv2.imshow("Cat 14", image14)
cv2.waitKey()
print("Чотирнадцятий Селкірк-рекс — кіт із кучерявою шерстю, ніби його завжди тільки-но причісували. Має спокійний, доброзичливий характер і виглядає дуже пухнастим, наче з мультфільму.")
#n = n - 1
rates[13] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face14:
    mask = mask.resize((w, h))
    cat14.paste(mask, (x, int(y + h / 3)), mask)
    cat14.save("cat_star14.png")
    cat_star14 = cv2.imread("cat_star14.png")
    cv2.imshow("Cat_star14", cat_star14)
    cv2.waitKey()

cv2.imshow("Cat 15", image15)
cv2.waitKey()
print("Останній та п'ятнадцятий - ЛаПерм — ще один кучерявий красень, але з м’якішою шерстю, що утворює милі хвилі. Дуже товариський і допитливий, любить бути в центрі уваги.")
#n = n - 1
rates[14] = int(input("Оцініть котика від 1 до 10: "))
for (x, y, w, h) in cat_face15:
    mask = mask.resize((w, h))
    cat15.paste(mask, (x, int(y + h / 3)), mask)
    cat15.save("cat_star15.png")
    cat_star15 = cv2.imread("cat_star15.png")
    cv2.imshow("Cat_star15", cat_star15)
    cv2.waitKey()


print("Тепер визначимось з результатами!")
cv2.imshow("Baraban", imageb)
print("Барабанний дрііііб.......")


if max(rates) == rates[0]:
    print("Огооо! Найбільше вам сподобався Мейн-кун")
    cv2.imshow("Cat 1", image1)
elif max(rates) == rates[1]:
    print("Огооо! Найбільше вам сподобався Сфінкс")
    cv2.imshow("Cat 2", image2)
elif max(rates) == rates[2]:
    print("Огооо! Найбільше вам сподобалась Шотландська висловуха")
    cv2.imshow("Cat 3", image3)
elif max(rates) == rates[3]:
    print("Огооо! Найбільше вам сподобався Бенгальський кіт")
    cv2.imshow("Cat 4", image4)
elif max(rates) == rates[4]:
    print("Огооо! Найбільше вам сподобалась Абіссінська кішка")
    cv2.imshow("Cat 5", image5)
elif max(rates) == rates[5]:
    print("Огооо! Найбільше вам сподобалась Персидська кішка")
    cv2.imshow("Cat 6", image6)
elif max(rates) == rates[6]:
    print("Огооо! Найбільше вам сподобалась Орієнтальна кішка")
    cv2.imshow("Cat 7", image7)
elif max(rates) == rates[7]:
    print("Огооо! Найбільше вам сподобався Бірманська кішка")
    cv2.imshow("Cat 8", image8)
elif max(rates) == rates[8]:
    print("Огооо! Найбільше вам сподобався Турецький ван")
    cv2.imshow("Cat 9", image9)
elif max(rates) == rates[9]:
    print("Огооо! Найбільше вам сподобався Рагдолл")
    cv2.imshow("Cat 10", image10)
elif max(rates) == rates[10]:
    print("Огооо! Найбільше вам сподобався Сіамський кіт")
    cv2.imshow("Cat 11", image11)
elif max(rates) == rates[11]:
    print("Огооо! Найбільше вам сподобався Корніш-рекс")
    cv2.imshow("Cat 12", image12)
elif max(rates) == rates[12]:
    print("Огооо! Найбільше вам сподобалась Норвезька лісова кішка")
    cv2.imshow("Cat 13", image13)
elif max(rates) == rates[13]:
    print("Огооо! Найбільше вам сподобався Селкірк-рекс")
    cv2.imshow("Cat 14", image14)
elif max(rates) == rates[14]:
    print("Огооо! Найбільше вам сподобався ЛаПерм")
    cv2.imshow("Cat 15", image15)



cv2.waitKey()


