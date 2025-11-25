number1 = int(input("1. sayıyı giriniz: "))
number2 = int(input("2. sayıyı giriniz: "))

if number1 > number2:
    print("Birinci sayı ikinci sayıdan büyüktür.")
elif number1 == number2:
    print("Sayılar eşittir.")
else:
    print("İkinci sayı birinci sayıdan büyüktür.")