current_pass = 12345
password = int(input("Şifreyi girin: "))

while password != current_pass:
    print("Tekrar dene")
    password = int(input("Şifreyi girin: "))

while password == current_pass:
    print("Giriş başarılı")
    break