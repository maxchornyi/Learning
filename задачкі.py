# Ex 1
human = 'life'
print(human)
human = 'death'
print(human)

# Ex 2
name = input("Type your name:")
print("Hello, " + name + " would you like to learn some Python today?")



# Ex 3
famous_person = 'Тарас Шевченко'
Sprichwort = '爱吧，  黑眉毛的姑娘们 但不要爱那些军官们， 军官们是些外乡人， 他们会恶毒地愚弄你们'
print(famous_person + '爱吧，黑眉毛的姑娘们，但不要爱那些军官们，军官们是些外乡人，他们会恶毒地愚弄你们' + Sprichwort)

# Ex.4
Name = " \t Max  \n  "
print(Name)
x = Name.lstrip()
print(x)
y = Name.rstrip()
print(y)
z = Name.strip()
print(z)

# Ex.5
print(' Maksym Chornyi \n Ukraine \n 58000 \n Chernivtsi \n Prospekt Nezalezhnosty \n 9999')
# Ex.6 + input
meters = float(input("Number "))
print(meters)
feet_meters = 3.28
inches_meters = 39.37
miles_meters = 0.00062137
feets = meters * feet_meters
inches = meters * inches_meters
miles = meters * miles_meters
print(feets)
print(inches)
print(miles)

# 7 +inptu
days = int(input("Type number "))
print(days)

seconds = days*24*60*60
print(seconds)
minutes = days*24*60
print(minutes)
hours = days*24
print(hours)

second = format(seconds, "10")
print(second)
min = format(minutes, "10")
print(min)
hour = format(hours, "10")
print(hour)

# 8+input
temperature = int(input("Type temperature "))
Celsium = temperature
Fahrenheit = temperature * 32 + 9/5
Kelvin = Celsium + 273.15
formatCelsium = format(Celsium, "14,.2f")
print(formatCelsium)
formatFahrenheit = format(Fahrenheit, "14,.2f")
print(formatFahrenheit)
formatKelvin = format(Kelvin, "14,.2f")
print(formatKelvin)

# 9+input
digit = input("any four-digit integer")
sum_digits = [int(x) for x in digit if x.isnumeric()]
print(sum_digits)
total = sum(sum_digits)
print(total)

# Ex 9 (my)

print('ex 9+')
Numberr = input("Type any 4 count")
Numberr = int(Numberr)
# розбиваємо число на цифри
thousands = Numberr // 1000
hundreds = (Numberr % 1000) // 100
tens = (Numberr % 100) // 10
ones = Numberr % 10
# знаходимо суму цифр
sum_of_digits = thousands + hundreds + tens + ones
# виводимо результат
print("{} + {} + {} + {} = {}".format(thousands, hundreds, tens, ones, sum_of_digits))

# Ex 10
import math

def distance(lat1, lon1, lat2, lon2):
    # Переводимо координати у радіани
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Радіус землі у кілометрах
    R = 6371.032
    # Обчислюємо відстань за формулою
    d = R * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    return  d
# Координати Пекіна
lat1, lon1 = 39.9075000, 116.3972300
# Координати Києва
lat2, lon2 = 50.4546600, 30.5238000
# Обчислюємо відстань між містами
dist = distance(lat1, lon1, lat2, lon2)
# Виводимо результат
print(f"Відстань між Пекіном і Києвом: {dist:.3f} км")
# Приклад використання для інших міст
city1 = (55.7558, 37.6173) # Москва
city2 = (48.8566, 2.3522) # Париж

dist = distance(*city1, *city2)
print(f"Відстань між Москвою і Парижем: {dist:.3f} км")
