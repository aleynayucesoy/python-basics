db = {
    "users": []
}

def add_user(name, age):
    try:
        age = int(age) 
    except ValueError:
        print("Lütfen gerçerli bir sayı giriniz.")
        return
    
    for u in db["users"]:
        if u["name"].lower() == name.lower():
            print("Bu kullanıcı zaten mevcut.")
            return
        
    db["users"].append({"name": name, "age": age})
    print(f"Kullanıcı '{name}' eklendi.")

def delete_user(name):
        initial_len = len(db["users"])
        db["users"] = [u for u in db["users"] if u["name"].lower() != name.lower()]

        if len(db["users"]) == initial_len:
            print("Kullanıcı bulunamadı.")
        else:
            print(f"Kullanıcı '{name}' silindi.")

def list_users():
        if not db["users"]:
            print("Kullanıcı bulunamadı.")
            return
        
        print("Kullanıcılar:")
        for u in db["users"]:
            print(f"- Ad: {u['name']}, Yaş: {u['age']}")

if __name__ == "__main__":
     while True:
        print("\n--- KULLANICI YÖNETİMİ ---")
        print("1. Kullanıcı Ekle")
        print("2. Kullanıcı Sil")
        print("3. Kullanıcıları Listele")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Adı: ")
            age = input("Yaşı: ")
            add_user(name, age)

        elif choice == "2":
            name = input("Silinecek kullanıcı: ")
            delete_user(name)

        elif choice == "3":
            list_users()

        elif choice == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

