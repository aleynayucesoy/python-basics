print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çıkış")

while True:
    choice = int(input("Yapmak istediğiniz işlemi seçin: "))
    
    if choice == 1:
        num1 = int(input("1. Sayıyı giriniz: "))
        num2 = int(input("2. Sayıyı giriniz: "))
        print(num1 + num2)
    elif choice == 2:
        num1 = int(input("1. Sayıyı giriniz: "))
        num2 = int(input("2. Sayıyı giriniz: "))
        print(num1 - num2)
    elif choice == 3:
        print("Çıkış Yapıldı.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")